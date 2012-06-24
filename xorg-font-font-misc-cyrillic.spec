Summary:	misc-cyrillic font
Summary(pl):	Font misc-cyrillic
Name:		xorg-font-font-misc-cyrillic
Version:	0.99.1
Release:	0.1
License:	MIT
Group:		Fonts
Source0:	http://xorg.freedesktop.org/releases/X11R7.0-RC3/font/font-misc-cyrillic-%{version}.tar.bz2
# Source0-md5:	71f5b4fcadf5dd156da186457f76058e
URL:		http://xorg.freedesktop.org/
BuildRequires:	autoconf >= 2.57
BuildRequires:	automake
BuildRequires:	pkgconfig >= 1:0.19
BuildRequires:	xorg-app-bdftopcf
BuildRequires:	xorg-app-mkfontdir
BuildRequires:	xorg-app-mkfontscale
BuildRequires:	xorg-font-font-util
BuildRequires:	xorg-util-util-macros
Requires(post,postun):	fontpostinst
Requires:	%{_fontsdir}/cyrillic
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
misc-cyrillic font.

%description -l pl
Font misc-cyrillic.

%prep
%setup -q -n font-misc-cyrillic-%{version}

%build
%{__aclocal}
%{__autoconf}
%{__automake}
%configure \
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
%doc COPYING ChangeLog
%{_fontsdir}/cyrillic/*.pcf.gz
