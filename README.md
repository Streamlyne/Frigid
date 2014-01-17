# Frigid

Frigid is a file control system. In it's first implementation
it will be capable of tracking files for changes. When a file 
changes it will be reverted to the stored state of the file.

Initially this will be done by storing copies of the files though
in future iterations of the applicaiton it will be useful to 
use git version control. 

### Commands
- `start`
- `stop`
- `restart`
- `freeze` | `add <file>`
- `thaw` | `remove <file>`

