Summary:	Fixed Cyrillic bitmap fonts
Summary(pl.UTF-8):	Fonty bitmapowe o stałej szerokości z cyrylicą
Name:		xorg-font-font-misc-cyrillic
Version:	1.0.4
Release:	1
License:	distributable (see COPYING)
Group:		Fonts
Source0:	https://xorg.freedesktop.org/releases/individual/font/font-misc-cyrillic-%{version}.tar.xz
# Source0-md5:	a21803eac9438a4d15d799d7afb68e01
URL:		https://xorg.freedesktop.org/
BuildRequires:	autoconf >= 2.60
BuildRequires:	automake
BuildRequires:	tar >= 1:1.22
BuildRequires:	xorg-app-bdftopcf
BuildRequires:	xorg-app-mkfontdir
BuildRequires:	xorg-app-mkfontscale
BuildRequires:	xorg-font-font-util >= 1.4
BuildRequires:	xorg-util-util-macros >= 1.20
BuildRequires:	xz
Requires(post,postun):	fontpostinst
Requires:	%{_fontsdir}/cyrillic
# contains useful aliases for these fonts
Requires:	xorg-font-font-alias >= 1.0.0
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Russian fixed Cyrillic bitmap fonts with KOI8-R encoding.

%description -l pl.UTF-8
Rosyjskie fonty bitmapowe o stałej szerokości znaków (fixed) z
cyrylicą w kodowaniu KOI8-R.

%prep
%setup -q -n font-misc-cyrillic-%{version}

%build
%{__aclocal}
%{__autoconf}
%{__automake}
%configure \
%if "%{_gnu}" != "-gnux32"
	--build=%{_host} \
	--host=%{_host} \
%endif
	--with-fontdir=%{_fontsdir}/cyrillic

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post
fontpostinst cyrillic

%postun
fontpostinst cyrillic

%files
%defattr(644,root,root,755)
%doc COPYING ChangeLog README.md
%{_fontsdir}/cyrillic/koi*.pcf.gz
