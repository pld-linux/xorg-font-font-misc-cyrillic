# $Rev: 3212 $, $Date: 2005-08-27 17:42:48 $
#
Summary:	font-misc-cyrillic
Summary(pl):	font-misc-cyrillic
Name:		xorg-font-font-misc-cyrillic
Version:	0.99.0
Release:	0.01
License:	MIT
Group:		X11
Source0:	http://xorg.freedesktop.org/X11R7.0-RC0/font/font-misc-cyrillic-%{version}.tar.bz2
# Source0-md5:	2a956bd0f7c456a75eebf2b406721ea2
URL:		http://xorg.freedesktop.org/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	xorg-app-bdftopcf
BuildRequires:	xorg-font-font-util
BuildRequires:	xorg-app-mkfontdir
BuildRequires:	xorg-app-mkfontscale
BuildRequires:	xorg-util-util-macros
BuildRequires:	pkgconfig >= 0.19
BuildRoot:	%{tmpdir}/font-misc-cyrillic-%{version}-root-%(id -u -n)

%description
font-misc-cyrillic

%description -l pl
font-misc-cyrillic


%prep
%setup -q -n font-misc-cyrillic-%{version}


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
%{_libdir}/X11/fonts/cyrillic/*
