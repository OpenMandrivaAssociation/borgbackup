Name:		borgbackup
Version:	1.4.3
Release:	1
Group:		Archiving/Backup
Summary:	Deduplicated backups
License:	BSD
URL:		https://borgbackup.github.io/
Source0:	https://pypi.io/packages/source/b/%{name}/%{name}-%{version}.tar.gz
#Patch0:	raise-dep.patch

BuildSystem:	python

BuildRequires:	pkgconfig(libacl)
BuildRequires:	pkgconfig(libb2)
BuildRequires:	pkgconfig(liblz4)
BuildRequires:	pkgconfig(libxxhash)
BuildRequires:	pkgconfig(libzstd)
BuildRequires:	pkgconfig(openssl)
BuildRequires:	pkgconfig(python)
BuildRequires:	python%{pyver}dist(cython)
BuildRequires:	python%{pyver}dist(llfuse)
BuildRequires:	python%{pyver}dist(msgpack)
BuildRequires:	python%{pyver}dist(pip)
BuildRequires:	python%{pyver}dist(pkgconfig)
BuildRequires:	python%{pyver}dist(pytest)
BuildRequires:	python%{pyver}dist(python-dateutil)
BuildRequires:	python%{pyver}dist(setuptools)
BuildRequires:	python%{pyver}dist(setuptools-scm)
BuildRequires:	python%{pyver}dist(sphinx)
BuildRequires:	python%{pyver}dist(sphinx-rtd-theme)
BuildRequires:	python%{pyver}dist(wheel)
Recommends:		python%{pyver}dist(llfuse)

%description
BorgBackup (short: Borg) is a deduplicating backup program.
Optionally, it supports compression and authenticated encryption.

The main goal of Borg is to provide an efficient and secure way to backup data.
The data deduplication technique used makes Borg suitable for daily backups
since only changes are stored. The authenticated encryption technique makes
it suitable for backups to not fully trusted targets.

%prep
%autosetup -n %{name}-%{version} -p1
# Remove upstream's egg-info
rm -vrf src/%{name}.egg-info

%build
export CLFAGS="%{optflags}"
export LDFLAGS="%{ldflags} -lpython%{py_ver}"
# disable msgpack version check - https://github.com/borgbackup/borg/issues/9109
#export BORG_MSGPACK_VERSION_CHECK=no
%py_build

%install
%py_install

%files
%{_bindir}/borg
%{_bindir}/borgfs
%{python_sitearch}/borg/
%{python_sitearch}/%{name}-%{version}.dist-info/
