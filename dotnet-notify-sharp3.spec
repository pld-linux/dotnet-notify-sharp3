# TODO:
# - check license
%include	/usr/lib/rpm/macros.mono
Summary:	notify-sharp is a C# client implementation for Desktop Notifications
Name:		dotnet-notify-sharp3
Version:	3.0.0
Release:	0.1
License:	X11/MIT
Group:		Development/Libraries
Source0:	https://www.meebey.net/projects/notify-sharp/downloads/notify-sharp-%{version}.tar.gz
# Source0-md5:	f3d84da137f6812ebada48c9adeaf01e
Patch0:		monodir.patch
URL:		https://www.meebey.net/projects/notify-sharp/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	dotnet-gtk-sharp3-devel
BuildRequires:	gtk+3-devel
BuildRequires:	libtool
BuildRequires:	mono-csharp
BuildRequires:	mono-devel
BuildRequires:	pkgconfig
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
notify-sharp is a C# client implementation for Desktop Notifications,
i.e. notification-daemon. It is inspired by the libnotify API.

Desktop Notifications provide a standard way of doing passive pop-up
notifications on the Linux desktop. These are designed to notify the
user of something without interrupting their work with a dialog box
that they must close. Passive popups can automatically disappear after
a short period of time.

%package devel
Summary:	Files required for compilation using notify-sharp
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Files required for compilation using notify-sharp.

%prep
%setup -q -n notify-sharp-%{version}
%patch0 -p1

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__automake}
%configure \
	--disable-docs

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README NEWS AUTHORS COPYING 
%dir %{_prefix}/lib/mono/gac/notify-sharp
%{_prefix}/lib/mono/gac/notify-sharp/*

%files devel
%defattr(644,root,root,755)
%dir %{_prefix}/lib/mono/notify-sharp
%{_prefix}/lib/mono/notify-sharp/*.dll
%{_pkgconfigdir}/notify-sharp-3.0.pc
