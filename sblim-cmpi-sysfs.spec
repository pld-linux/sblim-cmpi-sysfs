Summary:	SBLIM CMPI Linux Sysfs instrumentation
Summary(pl.UTF-8):	Przyrządy pomiarowe wpisów sysfs jądra Linuksa dla SBLIM CMPI
Name:		sblim-cmpi-sysfs
Version:	1.2.0
Release:	1
License:	Eclipse Public License v1.0
Group:		Libraries
Source0:	http://downloads.sourceforge.net/sblim/%{name}-%{version}.tar.bz2
# Source0-md5:	d74d41ac32b398f56044874fd448e291
URL:		http://sblim.sourceforge.net/
BuildRequires:	sblim-cmpi-base-devel
BuildRequires:	sblim-cmpi-devel
Requires:	%{name}-libs = %{version}-%{release}
Requires:	sblim-cmpi-base
Requires:	sblim-sfcb
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
SBLIM CMPI providers to expose the kernel devices accessible via
sysfs, which is a virtual filesystem in Linux kernel versions 2.5+
which provides a tree of system devices. The sysfs filesystem is 
mounted under /sys and the various subdirectories of /sys represent
the different classes of devices currently registered on the machine.

%description -l pl.UTF-8
Dostawcy informacji SBLIM CMPI udostępniający urządzenia jądra Linuksa
dostępne poprzez sysfs - wirtualny system plików w jądrach Linuksa
2.5+ udostępniający drzewo urządzeń systemowych. System plików sysfs
jest montowany w katalogu /sys, a różne jego podkatalogi reprezentują
różne klasy urządzeń aktualnie zarejestrowanych w systemie.

%prep
%setup -q

%build
%configure \
	CIMSERVER=sfcb \
	PROVIDERDIR=%{_libdir}/cmpi \
	--disable-static

%{__make} -j1

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -j1 install \
	DESTDIR=$RPM_BUILD_ROOT

# modules
%{__rm} $RPM_BUILD_ROOT%{_libdir}/cmpi/lib*.la
# API not exported
%{__rm} $RPM_BUILD_ROOT%{_libdir}/lib*.la
# packaged as %doc
%{__rm} -r $RPM_BUILD_ROOT%{_docdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%post
/sbin/ldconfig
%{_datadir}/%{name}/provider-register.sh \
	-r %{_datadir}/%{name}/Linux_Sysfs{Attribute,{Block,Bus,Input,Network,SCSI,SCSIHost,TTY}Device}.registration \
	-m %{_datadir}/%{name}/Linux_Sysfs{Attribute,{Block,Bus,Input,Network,SCSI,SCSIHost,TTY}Device}.mof >/dev/null

%preun
if [ "$1" = "0" ]; then
	%{_datadir}/%{name}/provider-register.sh -d \
		-r %{_datadir}/%{name}/Linux_Sysfs{Attribute,{Block,Bus,Input,Network,SCSI,SCSIHost,TTY}Device}.registration \
		-m %{_datadir}/%{name}/Linux_Sysfs{Attribute,{Block,Bus,Input,Network,SCSI,SCSIHost,TTY}Device}.mof >/dev/null
fi

%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS COPYING ChangeLog DEBUG NEWS README README.TEST sysfs.txt
%attr(755,root,root) %{_libdir}/libLinux_SysfsAttributeUtil.so
%attr(755,root,root) %{_libdir}/libLinux_SysfsDeviceUtil.so
%attr(755,root,root) %{_libdir}/cmpi/libLinux_SysfsAttribute.so
%attr(755,root,root) %{_libdir}/cmpi/libLinux_SysfsBlockDevice.so
%attr(755,root,root) %{_libdir}/cmpi/libLinux_SysfsBlockDeviceHasAttribute.so
%attr(755,root,root) %{_libdir}/cmpi/libLinux_SysfsBusDevice.so
%attr(755,root,root) %{_libdir}/cmpi/libLinux_SysfsBusDeviceHasAttribute.so
%attr(755,root,root) %{_libdir}/cmpi/libLinux_SysfsInputDevice.so
%attr(755,root,root) %{_libdir}/cmpi/libLinux_SysfsInputDeviceHasAttribute.so
%attr(755,root,root) %{_libdir}/cmpi/libLinux_SysfsNetworkDevice.so
%attr(755,root,root) %{_libdir}/cmpi/libLinux_SysfsNetworkDeviceHasAttribute.so
%attr(755,root,root) %{_libdir}/cmpi/libLinux_SysfsSCSIDevice.so
%attr(755,root,root) %{_libdir}/cmpi/libLinux_SysfsSCSIDeviceHasAttribute.so
%attr(755,root,root) %{_libdir}/cmpi/libLinux_SysfsSCSIHostDevice.so
%attr(755,root,root) %{_libdir}/cmpi/libLinux_SysfsSCSIHostDeviceHasAttribute.so
%attr(755,root,root) %{_libdir}/cmpi/libLinux_SysfsTTYDevice.so
%attr(755,root,root) %{_libdir}/cmpi/libLinux_SysfsTTYDeviceHasAttribute.so
%dir %{_datadir}/sblim-cmpi-sysfs
%{_datadir}/sblim-cmpi-sysfs/Linux_SysfsAttribute.mof
%{_datadir}/sblim-cmpi-sysfs/Linux_SysfsAttribute.registration
%{_datadir}/sblim-cmpi-sysfs/Linux_SysfsBlockDevice.mof
%{_datadir}/sblim-cmpi-sysfs/Linux_SysfsBlockDevice.registration
%{_datadir}/sblim-cmpi-sysfs/Linux_SysfsBusDevice.mof
%{_datadir}/sblim-cmpi-sysfs/Linux_SysfsBusDevice.registration
%{_datadir}/sblim-cmpi-sysfs/Linux_SysfsInputDevice.mof
%{_datadir}/sblim-cmpi-sysfs/Linux_SysfsInputDevice.registration
%{_datadir}/sblim-cmpi-sysfs/Linux_SysfsNetworkDevice.mof
%{_datadir}/sblim-cmpi-sysfs/Linux_SysfsNetworkDevice.registration
%{_datadir}/sblim-cmpi-sysfs/Linux_SysfsSCSIDevice.mof
%{_datadir}/sblim-cmpi-sysfs/Linux_SysfsSCSIDevice.registration
%{_datadir}/sblim-cmpi-sysfs/Linux_SysfsSCSIHostDevice.mof
%{_datadir}/sblim-cmpi-sysfs/Linux_SysfsSCSIHostDevice.registration
%{_datadir}/sblim-cmpi-sysfs/Linux_SysfsTTYDevice.mof
%{_datadir}/sblim-cmpi-sysfs/Linux_SysfsTTYDevice.registration
%attr(755,root,root) %{_datadir}/sblim-cmpi-sysfs/provider-register.sh
