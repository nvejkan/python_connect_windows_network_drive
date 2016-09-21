from contextlib import contextmanager
import os
'''
You should add some variables here:
username,password
'''
@contextmanager
def network_share_auth(share, username=None, password=None, drive_letter='P'):
    """Context manager that mounts the given share using the given
    username and password to the given drive letter when entering
    the context and unmounts it when exiting."""
    cmd_parts = ["NET USE %s: %s" % (drive_letter, share)]
    if password:
        cmd_parts.append(password)
    if username:
        cmd_parts.append("/USER:%s" % username)
    ret = os.system(" ".join(cmd_parts))
    if ret == 0:
        print('Drive:',drive_letter,'connected')
    try:
        yield
    finally:
        ret = os.system("NET USE %s: /DELETE /YES" % drive_letter)
        if ret == 0:
            print('Drive:',drive_letter,'disconnected')

def t_send_file(src_file,des_folder):
    # I hardcoded the network path as \\Network01\Docs
    with network_share_auth(r"\\Network01\Docs", username, password_drive,'T'):
        #folder = "T:/projects/ADR/Releases/Weekly WT Report"
        from shutil import copy2
        #copyfile(src, dst)
        print('copied : ',copy2(src_file, r"{0}/".format(des_folder)))

src_file = 'HLE.csv'
des_folder =  "T:/projects/XXX/Releases/Weekly WT Report"
t_send_file(src_file,des_folder)
