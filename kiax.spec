# TODO: use system's iaxclient instead of included one?
# - optflags
#
Summary:	IAX2 protocol telephony client
Summary(pl):	Klient protoko³u IAX2
Name:		kiax
Version:	0.8.5
Release:	2
License:	GPL v2
Group:		X11/Applications
Source0:	http://dl.sourceforge.net/kiax/%{name}-%{version}-src.tar.gz
# Source0-md5:	6bc7a9a94be7a3e998113311ce4e5847
Source1:	%{name}.png
Patch0:		%{name}-desktop.patch
Patch1:		%{name}-system_iaxclient_libs.diff
URL:		http://kiax.sourceforge.net/
BuildRequires:	qmake
BuildRequires:	qt-devel
BuildRequires:	qt-linguist
BuildRequires:	iaxclient-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
What is Kiax? - Kiax is an IAX client application (a so called
Softphone) which allows PC users to make ordinary VoIP calls to
Asterisk servers, the same way as they do it with their hardware
telephone. It aims to provide a simple and user-friendly graphical
interface and desktop integration for calling, contact list, call
register management and easy configuration. That is - a simple to use
IAX Client

%description -l pl
Czym jest Kiax? - Kiax jest klientem IAX (tak zwanym programowym
telefonem) pozwalaj±cym u¿ytkownikom PC wykonywaæ zwyk³e po³±czenia
VoIP do serwerów Asteriska tak, jakby dzia³o siê to ze sprzêtowymi
telefonami. Celem pakietu jest prosty i przyjazny dla u¿ytkownika
graficzny interfejs. To jest - prosty do u¿ycia klient IAX.

%prep
%setup -q -n %{name}-%{version}-src
%patch0 -p1
%patch1 -p1

%build
# not autoconf-generated
./configure \
	--prefix=%{_prefix}

%{__make} \
	QTDIR=/usr

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_datadir}/%{name}/{icons,i18n}}
install -d $RPM_BUILD_ROOT{%{_desktopdir},%{_pixmapsdir}}

install bin/kiax $RPM_BUILD_ROOT%{_bindir}
install icons/*.png $RPM_BUILD_ROOT%{_datadir}/%{name}/icons
install i18n/*.qm $RPM_BUILD_ROOT%{_datadir}/%{name}/i18n
install kiax.desktop $RPM_BUILD_ROOT%{_desktopdir}
install %{SOURCE1} $RPM_BUILD_ROOT%{_pixmapsdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGELOG README
%attr(755,root,root) %{_bindir}/%{name}
%{_datadir}/%{name}
%{_desktopdir}/%{name}.desktop
%{_pixmapsdir}/%{name}.png
