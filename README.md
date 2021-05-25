# WEFTPServer
### File Manager, FTP Server, Web Server and Echo Server on Python

## File Manager

### LdCommands (* - optional param):
* 1. hep - Show info about all commands [*command]
* 2. setrot - Set root dir [path]
* 3. getrot - Show root dir []
* 4. end - Exit from LdFileManager []
* 5. ind - Go in dir [name]
* 6. out - Out from dir []
* 7. lis - Show list files in directory []
* 8. credir - Create directory [name]
* 9. crefil - Create file [name]
* 10. rendir - Rename directory [oldname] [newname]
* 11. renfil - Rename file [oldname] [newname]
* 12. deldir - Delete directory [name]
* 13. delfil - Delete file [name]
* 14. copfil - Copy file [name] [newpath]
* 15. movfil - Move file [name] [newpath]
* 16. redfil - Read file [name] [*maxlines]
* 17. wrifil - Write file [name] [*append(1|0)]
* 18. wriend - Ends writing to file []

Note: Use brackets «[» and «]» for param with space on multiparams commands


## Echo Server

### Server - server.py
### Client - client.py
