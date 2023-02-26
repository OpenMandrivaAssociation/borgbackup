Name:           borgbackup
Version:        1.2.3
Release:        1
Group:          Archiving/Backup
Summary:        Deduplicated backups

License:        BSD
URL:            https://borgbackup.github.io/
Source0:        https://pypi.io/packages/source/b/%{pypi_name}/%{pypi_name}-%{version}.tar.gz

BuildRequires:  pkgconfig(libb2)
BuildRequires:  pkgconfig(libacl)
BuildRequires:  pkgconfig(libzstd)
BuildRequires:  pkgconfig(libxxhash)
BuildRequires:  pkgconfig(liblz4)
BuildRequires:  pkgconfig(openssl)
BuildRequires:  pkgconfig(python3)
BuildRequires:  python3dist(cython)
BuildRequires:  python3dist(llfuse)
BuildRequires:  python3dist(msgpack)
BuildRequires:  python3dist(pkgconfig)
BuildRequires:  python3dist(pytest)
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(setuptools-scm)
BuildRequires:  python3dist(sphinx)
BuildRequires:  python3dist(sphinx-rtd-theme)
BuildRequires:  python3dist(python-dateutil)
BuildRequires:  python3dist(wheel)
BuildRequires:  python3dist(pipe)
Recommends:     python3dist(llfuse)

%description
BorgBackup (short: Borg) is a deduplicating backup program.
Optionally, it supports compression and authenticated encryption.

The main goal of Borg is to provide an efficient and secure way to backup data.
The data deduplication technique used makes Borg suitable for daily backups
since only changes are stored. The authenticated encryption technique makes
it suitable for backups to not fully trusted targets.


%prep
%autosetup -p1
  
%build
%py_build
  
%py_install
  
%files
