<h1>EPAM DevOps Courses</h1>
<h2>Lab 2.2 AWS</h2>
<h3>Part A -- Base Objects Managment</h3>

<details><summary>1st VM named as EPAM_1 was created by wizard of Amazon Lightsail</summary><br>
<img src=t2.2_EPAM_1_ssh.PNG>
<img src=t2.2_EPAM_1_statIP_18.205.133.118.PNG></details>

<details><summary>2nd VM named as EPAM_2 was created by EC2 interface
as t2.micro instance</summary><br>
<img src=t2.2_EPAM_2_18.116.44.74.PNG>
<img src=t2.2_ssh_to_EPAM_2.PNG></details>

<details><summary>Snapshot of EPAM_2 was created</summary><br>
<img src=t2.2_EPAM_2_snapshot_menu.PNG>
<img src=t2.2_EPAM_2_snapshot_creation.PNG></details>

<details><summary>2 GiB volume was created in the same zone such 
EPAM_2 instance and then was attached to EPAM_2</summary><br>
<img src=t2.2_EPAM_2_new_volume_creation.PNG>
<img src=t2.2_EPAM_2_new_volume_attach_menu.PNG></details>

<details><summary>New volume was mounted as /disk_d in EPAM_2 instance,
few files was created in mounted FS</summary><br>
<img src=t2.2_EPAM_2_new_volume_mount.PNG></details>

<details><summary>New volume was unmonted and detached from EPAM_2 instance</summary><br>
<img src=t2.2_EPAM_2_new_volume_detach_menu.PNG></details>

<details><summary>New image was created and added to storage of new EPAM_3 instance</summary><br>
<img src=t2.2_EPAM_2_snapshot_to_image.PNG>
<img src=t2.2_EPAM_2_image_launch_for_EPAM_3.PNG>
<img src=t2.2_EPAM_3_add_storage_from_snapshot.PNG></details>

<details><summary>New volume was attached to EPAM_3 instance and mounted</summary><br>
<img src=t2.2_ssh_to_EPAM_3.PNG>
<img src=t2.2_EPAM_3_new_volume_mount.PNG></details>

<h3>Part B -- Application Extensions</h3>

<details><summary>EPAM_4-WP instance with WordPress was
created and configured (Amazon Lightsail)</summary><br>
<img src=t2.2b_WP_show_pwd.PNG>
<img src=t2.2b_WP_home_page.PNG>
<img src=t2.2b_WP_dns.PNG></details>

<details><summary>S3 repo was created, files stored in it and retrieved from it</summary><br>
<img src=t2.2b_S3_files_uploaded_in_new_backet.PNG></details>

<details><summary>AWS CLI was configured and used for files upload and download</summary><br>
<img src=t2.2b_IAM_add_new_user.PNG>
<img src=t2.2b_aws_configure_win64.PNG></details>

<details><summary>Docker container was created and launched</summary><br>
<img src=t2.2b_docker_installation.PNG>
<img src=t2.2b_docker_dockerfile.PNG>
<img src=t2.2b_docker_info.PNG>
<img src=t2.2b_docker_http_connection.PNG></details>

<details><summary>Docker container was pushed to Amazon ECR repo</summary><br>
<img src=t2.2b_docker_aws_repo_creation.PNG>
<img src=t2.2b_docker_aws_repo_push.PNG></details>
