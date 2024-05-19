# Manage authorization

## Objective:
To demonstrate your ability to manage file permissions using Linux commands, ensuring that users have the correct access rights to maintain a secure file system environment. This project will be part of your cybersecurity portfolio, showcasing your practical skills to prospective employers or recruiters.

## Scenario:
As a security professional at a large organization, you work closely with the research team. Your responsibilities include ensuring that file permissions are set correctly to protect sensitive data. You will examine existing file permissions, determine if they meet the required authorizations, and adjust them as needed to secure the system.

## Step by step 
#### 1. Check file and directory details:
   - Navigate to the `projects` directory and list its contents using `ls -l`.
   - Understand the output: Interpret the file type indicators and permissions shown.

#### 2. Analyze Current Permissions:
   - Review permissions for various files and directories within `projects`.
   - Identify any files with incorrect permissions, such as those granting unauthorized write access.

#### 3. Change file permissions:
   - **Task One:** Check for files granting write permissions to others and adjust accordingly.
   - **Task Two:** Modify permissions of specific files based on the identified issues.
   - **Task Three:** Address permissions on hidden files, ensuring proper access restrictions.
   - **Task Four:** Evaluate and adjust permissions on directories as needed to enforce security policies.

Throughout these tasks, permissions are modified using the `chmod` command, ensuring proper access control for users and groups while maintaining system integrity.

#### 1. Check file and directory details:
#### 1.1 Navigate to the `projects` Directory

```sh
researcher2@b3054688c4ab:~$ cd projects/
researcher2@b3054688c4ab:~/projects$
researcher2@b3054688c4ab:~/projects$ ls -l
total 20
drwx--x--- 2 researcher2 research_team 4096 May 19 04:45 drafts
-rw-rw-rw- 1 researcher2 research_team   46 May 19 04:45 project_k.txt
-rw-r----- 1 researcher2 research_team   46 May 19 04:45 project_m.txt
-rw-rw-r-- 1 researcher2 research_team   46 May 19 04:45 project_r.txt
-rw-rw-r-- 1 researcher2 research_team   46 May 19 04:45 project_t.txt
```
#### 1.2 Understand the Output

The output of `ls -l` provides several columns of information:

- The first column indicates the type of file and permissions.
  - `d` denotes a directory.
  - `-` denotes a regular file.
  
#### 2. Analyze Current Permissions:
- **drafts**: `drwx--x---`
  - Owner: researcher2 (read, write, execute)
  - Group: research_team (execute only)
  - Others: no permissions

- **project_k.txt**: `-rw-rw-rw-`
  - Owner: researcher2 (read, write)
  - Group: research_team (read, write)
  - Others: read, write

- **project_m.txt**: `-rw-r-----`
  - Owner: researcher2 (read, write)
  - Group: research_team (read only)
  - Others: no permissions

- **project_r.txt**: `-rw-rw-r--`
  - Owner: researcher2 (read, write)
  - Group: research_team (read, write)
  - Others: read only

- **project_t.txt**: `-rw-rw-r--`
  - Owner: researcher2 (read, write)
  - Group: research_team (read, write)
  - Others: read only
  
#### 3. Change file permissions:
 - **Task One:** Check for files granting write permissions to others and adjust accordingly.
**Which file grants other users write permissions?**<br>
``Answer: The project_k.txt file has write permissions for other users.``<br>
- **Task Two:** Modify permissions of specific files based on the identified issues.
```sh
researcher2@b3054688c4ab:~/projects$ chmod o-w project_k.txt
researcher2@b3054688c4ab:~/projects$ ls -l
total 20
drwx--x--- 2 researcher2 research_team 4096 May 19 04:45 drafts
-rw-rw-r-- 1 researcher2 research_team   46 May 19 04:45 project_k.txt
-rw-r----- 1 researcher2 research_team   46 May 19 04:45 project_m.txt
-rw-rw-r-- 1 researcher2 research_team   46 May 19 04:45 project_r.txt
-rw-rw-r-- 1 researcher2 research_team   46 May 19 04:45 project_t.txt
```
**What are the group permissions on the project_m.txt file?**<br>
``Answer: The group permissions of the project_m.txt file is read only.``

- **Task three:** Use the chmod command to change permissions of the project_m.txt file so that the group doesn’t have read or write permissions.
```sh
researcher2@b3054688c4ab:~/projects$ chmod g-r project_m.txt
researcher2@b3054688c4ab:~/projects$ ls -l
total 20
drwx--x--- 2 researcher2 research_team 4096 May 19 04:45 drafts
-rw-rw-r-- 1 researcher2 research_team   46 May 19 04:45 project_k.txt
-rw------- 1 researcher2 research_team   46 May 19 04:45 project_m.txt
-rw-rw-r-- 1 researcher2 research_team   46 May 19 04:45 project_r.txt
-rw-rw-r-- 1 researcher2 research_team   46 May 19 04:45 project_t.txt
```

- **Task four:** Change file permissions on a hidden file
***Check the permissions of the hidden file ```.project_x.txt``` and answer the question that follows.***
```sh
researcher2@b3054688c4ab:~/projects$ ls -la
total 32
drwxr-xr-x 3 researcher2 research_team 4096 May 19 04:45 .
drwxr-xr-x 3 researcher2 research_team 4096 May 19 05:06 ..
-rw--w---- 1 researcher2 research_team   46 May 19 04:45 .project_x.txt
drwx--x--- 2 researcher2 research_team 4096 May 19 04:45 drafts
-rw-rw-r-- 1 researcher2 research_team   46 May 19 04:45 project_k.txt
-rw------- 1 researcher2 research_team   46 May 19 04:45 project_m.txt
-rw-rw-r-- 1 researcher2 research_team   46 May 19 04:45 project_r.txt
-rw-rw-r-- 1 researcher2 research_team   46 May 19 04:45 project_t.txt
```
***Which owner type has the incorrect write permissions?***
``Answer: The user and group owner types have incorrect write permissions.``

***Change the permissions of the file .project_x.txt so that both the user and the group can read, but not write to, the file.***<br>
```sh
researcher2@b3054688c4ab:~/projects$ chmod u-w,g-w,g+r .project_x.txt
researcher2@b3054688c4ab:~/projects$ ls -la
total 32
drwxr-xr-x 3 researcher2 research_team 4096 May 19 04:45 .
drwxr-xr-x 3 researcher2 research_team 4096 May 19 05:06 ..
-r--r----- 1 researcher2 research_team   46 May 19 04:45 .project_x.txt
drwx--x--- 2 researcher2 research_team 4096 May 19 04:45 drafts
-rw-rw-r-- 1 researcher2 research_team   46 May 19 04:45 project_k.txt
-rw------- 1 researcher2 research_team   46 May 19 04:45 project_m.txt
-rw-rw-r-- 1 researcher2 research_team   46 May 19 04:45 project_r.txt
-rw-rw-r-- 1 researcher2 research_team   46 May 19 04:45 project_t.txt
```
- **Task five:** Change directory permissions***

***Check the permissions of the drafts directory and answer the following question.***
```sh
researcher2@b3054688c4ab:~/projects$ ls -l 
total 20
drwx--x--- 2 researcher2 research_team 4096 May 19 04:45 drafts
-rw-rw-r-- 1 researcher2 research_team   46 May 19 04:45 project_k.txt
-rw------- 1 researcher2 research_team   46 May 19 04:45 project_m.txt
-rw-rw-r-- 1 researcher2 research_team   46 May 19 04:45 project_r.txt
-rw-rw-r-- 1 researcher2 research_team   46 May 19 04:45 project_t.txt
```
****Does the group have permissions set to access the drafts directory and its contents?****<br>
``Answer: Yes, the group has execute permissions and therefore has access to the drafts directory.``
****Remove the execute permission for the group from the drafts directory.****
```sh
researcher2@b3054688c4ab:~/projects$ chmod g-x drafts
researcher2@b3054688c4ab:~/projects$ ls -l
total 20
drwx------ 2 researcher2 research_team 4096 May 19 04:45 drafts
-rw-rw-r-- 1 researcher2 research_team   46 May 19 04:45 project_k.txt
-rw------- 1 researcher2 research_team   46 May 19 04:45 project_m.txt
-rw-rw-r-- 1 researcher2 research_team   46 May 19 04:45 project_r.txt
-rw-rw-r-- 1 researcher2 research_team   46 May 19 04:45 project_t.txt
```

