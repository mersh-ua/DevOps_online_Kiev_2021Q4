# EPAM DevOps Curses
## Lab 5.2 UNIX / How to manage user accounts. Understanding file permissions (modes) in UNIX.

<details><summary>/etc/passwd and /etc/group</summary>
<br><p>There are two main files that are used to separate privileges.
<p>They contain information about user and group names and their corresponding numeric identifiers (UID and GID). The user is a member of one or more groups. /etc/passwd contains the GID of the user's primary group, additional groups for this user are listed in /etc/group:

![](t5.2.passwd.group.png)
</details>

<details><summary>useradd and usermod</summary>
<br><p>We can use the adduser or useradd commands to add a user. You can change the properties of a user account using the usermod command. /etc/skel/ contains base files for user's home directory:

![](t5.2.user.add.png)
![](t5.2.user.mod.skel.modes.png)
</details>

<details><summary>chmod, chown and chgrp</summary>
<br><p>Every file in UNIX has 3 basic permissions: Read, Write and eXecute

![](t5.2.ch.own.grp.PNG)
![](t5.2.passwd+group-r.PNG)
<p>Every file in UNIX has 4 sets of these permissions: for special bits, for owner, for group and for others

![](t5.2.owner.group.others.PNG)
![](t5.2.SUID+t.PNG)
</details>

<details><summary>umask</summary>
<br><p>You can define the value of file permissions (modes) by default. You wiil know that umask work with directories in another way like as other files.

![](t5.2.umask.PNG)
</details>
