Summary:	xauth - X authority file utility
Summary(pl.UTF-8):	xauth - narzędzie do plików X authority
Name:		xorg-app-xauth
Version:	1.0.5
Release:	1
License:	MIT
Group:		X11/Applications
Source0:	http://xorg.freedesktop.org/releases/individual/app/xauth-%{version}.tar.bz2
# Source0-md5:	46fc44e5e947d3720f3be5054044ff0e
URL:		http://xorg.freedesktop.org/
BuildRequires:	autoconf >= 2.60
BuildRequires:	automake
BuildRequires:	pkgconfig >= 1:0.19
BuildRequires:	xorg-lib-libXau-devel
BuildRequires:	xorg-lib-libXext-devel
# just xmuu
BuildRequires:	xorg-lib-libXmu-devel
BuildRequires:	xorg-lib-xtrans-devel
BuildRequires:	xorg-util-util-macros >= 1.8
Obsoletes:	X11-xauth < 1:7.0.0
Obsoletes:	XFree86-xauth < 1:7.0.0
Obsoletes:	xauth < 1:7.0.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The xauth program is used to edit and display the authorization
information used in connecting to the X server. This program is
usually used to extract authorization records from one machine and
merge them in on another (as is the case when using remote logins or
granting access to other users).

%description -l pl.UTF-8
Program xauth służy do edycji i wyświetlania informacji
autoryzacyjnych używanych przy łączeniu z X serwerem. Ten program
przeważnie jest używany do wyciągania rekordów autoryzacji z jednej
maszyny i dołączania ich na innej (w celu umożliwienia zdalnego
logowania lub udostępnienia innym użytkownikom).

%prep
%setup -q -n xauth-%{version}

%build
%{__aclocal}
%{__autoconf}
%{__autoheader}
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
%doc COPYING ChangeLog README
%attr(755,root,root) %{_bindir}/xauth
%{_mandir}/man1/xauth.1x*
