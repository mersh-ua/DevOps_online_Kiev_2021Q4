# EPAM DevOps Curses
## Lab 5.1 UNIX
### Part A

<details><summary>How to make logon to system, change password and use man</summary>

![](t5.1.A.login.PNG)
![](t5.1.A.bashrc.ls.w.PNG)
![](t5.1.A.man.wc.passwd.PNG)

</details>

### Part B

<details><summary>Basics of UNIX file system, search and navigation</summary>

ls is a very useful and powerful utility like many other UNIX utilities such as cp, rm and cat. Bash have several built-in commands such as cd or pwd that we need every day.

![](t5.1.B.tree.root.PNG)
![](t5.1.B.file.ls.rel.abs.pahtes.PNG)
![](t5.1.B.5.PNG)

We use the same ln command to creation of hard and soft links.

![](t5.1.B.6.PNG)

Size of symbolic link file is equal for length of target file name. In our example above length of target file name is 8 (labwork2).<br>
The symbolic link will be broken if the target file is deleted.<p>
In the example below we use the tee utility to duplicate the output of another command (on the left of tee) to the console. This command is inside the pipeline but first we see its output. This is because bash have to wait when pipeline done.

![](t5.1.B.locate.df.grep.tee.PNG)
![](t5.1.B.find_host.PNG)
![](t5.1.B.find_ss.less.PNG)
![](t5.1.B.13.PNG)

</details>
