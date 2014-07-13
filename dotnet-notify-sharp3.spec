%include	/usr/lib/rpm/macros.mono
Summary:	C# client implementation for Desktop Notifications
Summary(pl.UTF-8):	Implementacja C# klienta usługi Desktop Notifications
Name:		dotnet-notify-sharp3
Version:	3.0.0
Release:	1
License:	MIT
Group:		Development/Libraries
Source0:	https://www.meebey.net/projects/notify-sharp/downloads/notify-sharp-%{version}.tar.gz
# Source0-md5:	f3d84da137f6812ebada48c9adeaf01e
Patch0:		monodir.patch
URL:		https://www.meebey.net/projects/notify-sharp/
BuildRequires:	autoconf >= 2.50
BuildRequires:	automake
BuildRequires:	dotnet-dbus-sharp-devel >= 1:0.7
BuildRequires:	dotnet-dbus-sharp-glib-devel >= 0.5
BuildRequires:	dotnet-gtk-sharp3-devel >= 2.99.1
BuildRequires:	gtk+3-devel
BuildRequires:	mono-csharp >= 1.1.13
BuildRequires:	mono-devel >= 1.1.13
BuildRequires:	mono-monodoc >= 1.1.18
BuildRequires:	pkgconfig
Requires:	dotnet-dbus-sharp >= 1:0.7
Requires:	dotnet-dbus-sharp-glib >= 0.5
Requires:	dotnet-gtk-sharp3 >= 2.99.1
Requires:	mono >= 1.1.13
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
notify-sharp (Notify#) is a C# client implementation for Desktop
Notifications, i.e. notification-daemon. It is inspired by the
libnotify API.

Desktop Notifications provide a standard way of doing passive pop-up
notifications on the Linux desktop. These are designed to notify the
user of something without interrupting their work with a dialog box
that they must close. Passive popups can automatically disappear after
a short period of time.

%description -l pl.UTF-8
notify-sharp (Notify#) to implementacja w C# klienta usługi Desktop
Notifications (powiadomień w środowisku graficznym), tj. usługi
notification-daemon. Jest zainspirowana API biblioteki libnotify.

Desktop Notifications to usługa zapewniająca standardową metodę
wykonywania pasywnych powiadomień poprzez wyskakujące okienka na
pulpicie Linuksa. Jest zaprojektowana w celu powiadamiania użytkownika
o jakimś zdarzeniu bez przerywania pracy oknem dialogowym, które
trzeba zamknąć. Pasywne wyskakujące okienka mogą znikać automatycznie
po krótkim okresie czasu.

%package devel
Summary:	Development files for notify-sharp library
Summary(pl.UTF-8):	Pliki programistyczne biblioteki notify-sharp
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	dotnet-gtk-sharp3-devel >= 2.99.1
Requires:	mono-devel >= 1.1.13

%description devel
Development files for notify-sharp library.

%description devel -l pl.UTF-8
Pliki programistyczne biblioteki notify-sharp.

%prep
%setup -q -n notify-sharp-%{version}
%patch0 -p1

%build
%{__aclocal}
%{__autoconf}
%{__automake}
%configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS COPYING ChangeLog NEWS README
%dir %{_prefix}/lib/mono/gac/notify-sharp
%{_prefix}/lib/mono/gac/notify-sharp/3.0.0.0__*

%files devel
%defattr(644,root,root,755)
%dir %{_prefix}/lib/mono/notify-sharp
%{_prefix}/lib/mono/notify-sharp/notify-sharp.dll
%{_prefix}/lib/monodoc/sources/notify-sharp-3-docs.*
%{_pkgconfigdir}/notify-sharp-3.0.pc
