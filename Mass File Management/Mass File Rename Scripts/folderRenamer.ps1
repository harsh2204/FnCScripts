Get-ChildItem -Directory -Recurse | Rename-Item  -NewName {$_.Name -replace 'this','with that'}
