%global ldscriptdir %{_datadir}/%{name}/ldscripts

Name: 		libhugetlbfs
Version: 	2.22
Release: 	4
Summary: 	A library which provides easy access to huge pages of memory
License: 	LGPLv2+
URL: 		https://github.com/libhugetlbfs/libhugetlbfs
Source0: 	https://github.com/libhugetlbfs/libhugetlbfs/releases/download/%{version}/%{name}-%{version}.tar.gz

Patch0000: 	0000-build_flags.patch

Patch9000:	libhugetlbfs-2.16-remap_segments_with_MAP_SHARED.patch
Patch9001:	libhugetlbfs-2.16-remap_segments_with_MAP_SHARED-2.patch
Patch9002:	libhugetlbfs-make-cflags.patch
Patch9003:	libhugetlbfs-fix-max-segment-cannot-adopt-the-x86.patch

Recommends:	%{name}-help = %{version}-%{release}
BuildRequires: 	gcc glibc-devel glibc-static

%description
The libhugetlbfs package interacts with the Linux hugetlbfs to make large
pages available to applications in a transparent manner.The library also
comes with several userspace tools to help with huge page usability,
environment setup, and control.

%package 	devel
Summary:	The devel for %{name}
Requires:	%{name} = %{version}-%{release}
%description 	devel
Header files for libhugetlbfs

%package 	utils
Summary:	The utils for %{name}
Requires:	%{name} = %{version}-%{release}
%description utils
Userspace utilities for configuring the hugepage environment

%package_help

%prep
%autosetup -n %{name}-%{version} -p1

%build
%set_build_flags
make BUILDTYPE=NATIVEONLY

%install
%make_install PREFIX=%{_prefix} LDSCRIPTDIR=%{ldscriptdir} BUILDTYPE=NATIVEONLY
make install-helper PREFIX=%{_prefix} DESTDIR=$RPM_BUILD_ROOT LDSCRIPTDIR=%{ldscriptdir} BUILDTYPE=NATIVEONLY
mkdir -p -m755 $RPM_BUILD_ROOT%{_sysconfdir}/security/limits.d
touch $RPM_BUILD_ROOT%{_sysconfdir}/security/limits.d/hugepages.conf

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%license LGPL-2.1
%{_libdir}/libhugetlbfs.so*
%{_datadir}/%{name}/
%ghost %config(noreplace) %{_sysconfdir}/security/limits.d/hugepages.conf
%exclude %{_libdir}/libhugetlbfs_privutils.so
%exclude %{_libdir}/*.a

%files devel
%{_includedir}/hugetlbfs.h

%files utils
%{_bindir}/hugeedit
%{_bindir}/hugeadm
%{_bindir}/hugectl
%{_bindir}/pagesize
%{_bindir}/huge_page_setup_helper.py
%exclude %{_bindir}/cpupcstat
%exclude %{_bindir}/oprofile_map_events.pl
%exclude %{_bindir}/oprofile_start.sh
%exclude %{_libdir}/perl5/TLBC

%files help
%doc README HOWTO NEWS
%{_mandir}/man1/*.gz
%{_mandir}/man3/*.gz
%{_mandir}/man7/libhugetlbfs.7.gz
%{_mandir}/man8/*.gz


%changelog
* Mon Feb 8 2021 xinghe <xinghe1@huawei.com> - 2.22-4
- rebuild package

* Tue Dec 15 2020 wuxu<wuxu.wu@hotmail.com> - 2.22-3
- Type:enhancement
- ID:NA
- SUG:restart
- DESC: fix max segment cannot adopt the x86

* Wed Nov 11 2020 xinghe <xinghe1@huawei.com> - 2.22-2
- add help for Recommends

* Fri Apr 24 2020 lihongjiang<lihongjiang6@huawei.com> - 2.22-1
- Type:enhancement
- ID:NA
- SUG:restart
- DESC:update version to 2.22

* Tue Feb 25 2020 lihongjiang<lihongjiang6@huawei.com> - 2.20-14
- Type:enhancement
- ID:NA
- SUG:restart
- DESC:change script from py2 to py3

* Mon Dec 30 2019 lihongjiang<lihongjiang6@huawei.com> - 2.20-13
- Type:enhancement
- ID:NA
- SUG:restart
- DESC:update source code

* Mon Dec 30 2019 lihongjiang<lihongjiang6@huawei.com> - 2.20-12
- Type:enhancement
- ID:NA
- SUG:restart
- DESC:update spec

* Mon Apr 22 2019 lihongjiang<lihongjiang6@huawei.com> - 2.20-11
- Type:enhancement
- ID:NA
- SUG:restart
- DESC:fix-tests-with-heapshrink-fail

* Thu Mar 21 2019 lihongjiang<lihongjiang6@huawei.com> - 2.20-10
- Type:enhancement
- ID:NA
- SUG:restart
- DESC:backport patches

* Tue Jan 22 2019 xiashuang<xiashuang1@huawei.com> - 2.20-9
- Type:enhancement
- ID:NA
- SUG:restart
- DESC:sync patches from 7.3

* Sat Jul 18 2018 openEuler Buildteam <buildteam@openeuler.org> - 2.20-8
- Package init
