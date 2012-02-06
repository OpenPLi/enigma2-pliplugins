import os, commands
from collections import namedtuple

_ntuple_diskusage = namedtuple('diskusage', 'total used free')

def enum(*sequential, **named):
    enums = dict(zip(sequential, range(len(sequential))), **named)
    return type('Enum', (), enums)

DiskInfoTypes = enum('totalmounts', 'mountpoint', 'filesystem', 'used', 'avail','total')

def disk_usage(path):
    st = os.statvfs(path)
    free = st.f_bavail * st.f_frsize
    total = st.f_blocks * st.f_frsize
    used = (st.f_blocks - st.f_bfree) * st.f_frsize
    return _ntuple_diskusage(total, used, free)

def GetDiskInfo(infotype, devindex):
	try:
		dfoutput = commands.getoutput('df').split('\n')

		if infotype == DiskInfoTypes.totalmounts:
			return len(dfoutput)-1
		elif infotype == DiskInfoTypes.mountpoint:
			return dfoutput[devindex+1].split()[5]
		elif infotype == DiskInfoTypes.filesystem:
			return dfoutput[devindex+1].split()[0]

		myusage = disk_usage(dfoutput[devindex+1].split()[5])

		if infotype == DiskInfoTypes.used:
			return long(myusage.used)/1024
		elif infotype == DiskInfoTypes.avail:
			return long(myusage.free)/1024
		elif infotype == DiskInfoTypes.total:
			return long(myusage.total)/1024
		return 0
	except:
		return 0
