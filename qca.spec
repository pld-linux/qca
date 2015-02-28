# TODO:
# - fix chrpath
#
# chrpath stripping fails
%define	no_install_post_chrpath	1
Summary:	Qt Cryptographic Architecture (QCA) Library
Summary(pl.UTF-8):	Biblioteka Qt Cryptographic Architecture (QCA)
Name:		qca
Version:	2.0.3
Release:	3
License:	LGPL v2.1
Group:		Libraries
Source0:	http://delta.affinix.com/download/qca/2.0/%{name}-%{version}.tar.bz2
# Source0-md5:	fc15bd4da22b8096c51fcfe52d2fa309
Patch0:		%{name}-gcc47.patch
URL:		http://delta.affinix.com/qca/
BuildRequires:	QtCore-devel
BuildRequires:	QtGui-devel
BuildRequires:	QtNetwork-devel
BuildRequires:	QtTest-devel
BuildRequires:	libstdc++-devel
BuildRequires:	openssl-devel >= 0.9.7d
BuildRequires:	qt4-build >= 4.3.3-3
BuildRequires:	qt4-qmake >= 4.3.3-3
BuildRequires:	which
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Qt Cryptographic Architecture (QCA) Library.

%description -l pl.UTF-8
Biblioteka Qt Cryptographic Architecture (QCA).

%package devel
Summary:	Qt Cryptographic Architecture (QCA) Library - development files
Summary(pl.UTF-8):	Biblioteka Qt Cryptographic Architecture (QCA) - pliki dla programistów
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	QtCore-devel

%description devel
Qt Cryptographic Architecture (QCA) Library - development files.

%description devel -l pl.UTF-8
Biblioteka Qt Cryptographic Architecture (QCA) - pliki dla
programistów.

%prep
%setup -q
%patch0 -p1

%build
./configure \
	--prefix=%{_prefix} \
	--libdir=%{_libdir} \
	--datadir=%{_datadir}
qmake-qt4
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	INSTALL_ROOT=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc README
%attr(755,root,root) %{_bindir}/qcatool2
%ghost %attr(755,root,root) %{_libdir}/libqca.so.2
%attr(755,root,root) %{_libdir}/libqca.so.*.*
%{_mandir}/man1/*.1*
%{_datadir}/qca

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libqca.so
%{_includedir}/QtCrypto
%{_pkgconfigdir}/*.pc
%{_libdir}/libqca.prl
%{_datadir}/qt4/mkspecs/features/crypto.prf
