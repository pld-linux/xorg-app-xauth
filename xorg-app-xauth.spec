Summary:	xauth - X authority file utility
Summary(pl):	xauth - narzêdzie do plików X authority
Name:		xorg-app-xauth
Version:	1.0.1
Release:	1
License:	MIT
Group:		X11/Applications
Source0:	http://xorg.freedesktop.org/releases/individual/app/xauth-%{version}.tar.bz2
# Source0-md5:	ed848ebba8d3a1ca727b80d6b89dc3c3
URL:		http://xorg.freedesktop.org/
BuildRequires:	autoconf >= 2.57
BuildRequires:	automake
BuildRequires:	pkgconfig >= 1:0.19
BuildRequires:	xorg-lib-libXau-devel
BuildRequires:	xorg-lib-libXext-devel
# just xmuu
BuildRequires:	xorg-lib-libXmu-devel
BuildRequires:	xorg-lib-xtrans-devel
BuildRequires:	xorg-util-util-macros >= 0.99.2
Obsoletes:	X11-xauth
Obsoletes:	XFree86-xauth
Obsoletes:	xauth
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The xauth program is used to edit and display the authorization
information used in connecting to the X server. This program is
usually used to extract authorization records from one machine and
merge them in on another (as is the case when using remote logins or
granting access to other users).

%description -l pl
Program xauth s³u¿y do edycji i wy¶wietlania informacji
autoryzacyjnych u¿ywanych przy ³±czeniu z X serwerem. Ten program
przewa¿nie jest u¿ywany do wyci±gania rekordów autoryzacji z jednej
maszyny i do³±czania ich na innej (w celu umo¿liwienia zdalnego
logowania lub udostêpnienia innym u¿ytkownikom).

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
%doc COPYING ChangeLog
%attr(755,root,root) %{_bindir}/xauth
%{_mandir}/man1/xauth.1x*
