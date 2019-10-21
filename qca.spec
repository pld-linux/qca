Summary:	Qt Cryptographic Architecture (QCA) Library
Summary(pl.UTF-8):	Biblioteka Qt Cryptographic Architecture (QCA)
Name:		qca
Version:	2.1.3
Release:	4
License:	LGPL v2.1
Group:		Libraries
Source0:	http://download.kde.org/stable/qca/%{version}/src/%{name}-%{version}.tar.xz
# Source0-md5:	5019cc29efcf828681cd93164238ce26
Patch0:		openssl.patch
Patch1:		qt5.patch
URL:		http://delta.affinix.com/qca/
BuildRequires:	Qt5Core-devel
BuildRequires:	Qt5Gui-devel
BuildRequires:	Qt5Network-devel
BuildRequires:	Qt5Test-devel
BuildRequires:	QtCore-devel
BuildRequires:	QtGui-devel
BuildRequires:	QtNetwork-devel
BuildRequires:	QtTest-devel
BuildRequires:	cmake >= 2.8.2
BuildRequires:	libstdc++-devel
BuildRequires:	nss-devel
BuildRequires:	openssl-devel >= 0.9.7d
BuildRequires:	qt4-build >= 4.3.3-3
BuildRequires:	qt4-qmake >= 4.3.3-3
BuildRequires:	qt5-build
BuildRequires:	which
Provides:	qt4-plugin-qca-ossl = %{version}
Obsoletes:	qt4-plugin-qca-cyrus-sasl
Obsoletes:	qt4-plugin-qca-gnupg
Obsoletes:	qt4-plugin-qca-ossl
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

%package -n qca-qt5
Summary:	Qt Cryptographic Architecture (QCA) Library
Summary(pl.UTF-8):	Biblioteka Qt Cryptographic Architecture (QCA)
Group:		Libraries
URL:		http://download.kde.org/stable/qca/

%description -n qca-qt5
Qt Cryptographic Architecture (QCA) Library. qt5 version

%description -n qca-qt5 -l pl.UTF-8
Biblioteka Qt Cryptographic Architecture (QCA).

%package -n qca-qt5-devel
Summary:	Qt Cryptographic Architecture (QCA) Library - development files
Summary(pl.UTF-8):	Biblioteka Qt Cryptographic Architecture (QCA) - pliki dla programistów
Group:		Development/Libraries
Requires:	QtCore-devel
Requires:	qca-qt5 = %{version}-%{release}

%description -n qca-qt5-devel
Qt Cryptographic Architecture (QCA) Library - development files.

%description -n qca-qt5-devel -l pl.UTF-8
Biblioteka Qt Cryptographic Architecture (QCA) - pliki dla
programistów.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

%build
install -d build4
cd build4
QC_CERTSTORE_PATH=/etc/certs/ca-certificates.crt; export QC_CERTSTORE_PATH
%cmake \
	-DQCA_LIBRARY_INSTALL_DIR=%{_libdir} \
	-DQCA_FEATURE_INSTALL_DIR=%{_datadir}/qt4/mkspecs/features/ \
	-DQT4_BUILD=ON \
	..
%{__make}
cd ..

install -d build5
cd build5
%cmake \
	-DQCA_INSTALL_IN_QT_PREFIX=ON \
	-DQCA_MAN_INSTALL_DIR=%{_mandir} \
	..
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} -C build4 install \
	DESTDIR=$RPM_BUILD_ROOT

%{__make} -C build5 install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun -p /sbin/ldconfig

%post -n qca-qt5 -p /sbin/ldconfig
%postun -n qca-qt5 -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc README
%attr(755,root,root) %{_bindir}/qcatool
%attr(755,root,root) %{_bindir}/mozcerts
%ghost %attr(755,root,root) %{_libdir}/libqca.so.2
%attr(755,root,root) %{_libdir}/libqca.so.*.*
%dir %{_libdir}/qca
%dir %{_libdir}/qca/crypto
%attr(755,root,root) %{_libdir}/qca/crypto/libqca-cyrus-sasl.so
%attr(755,root,root) %{_libdir}/qca/crypto/libqca-gcrypt.so
%attr(755,root,root) %{_libdir}/qca/crypto/libqca-gnupg.so
%attr(755,root,root) %{_libdir}/qca/crypto/libqca-logger.so
%attr(755,root,root) %{_libdir}/qca/crypto/libqca-nss.so
%attr(755,root,root) %{_libdir}/qca/crypto/libqca-ossl.so
%attr(755,root,root) %{_libdir}/qca/crypto/libqca-softstore.so
%{_mandir}/man1/qcatool.1*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libqca.so
%{_includedir}/QtCrypto
%{_pkgconfigdir}/qca2.pc
%{_datadir}/qt4/mkspecs/features/crypto.prf
%{_libdir}/cmake/Qca

%files -n qca-qt5
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/qt5/bin/mozcerts-qt5
%attr(755,root,root) %{_libdir}/qt5/bin/qcatool-qt5
#%{_prefix}/certs/rootcerts.pem
%attr(755,root,root) %ghost %{_libdir}/libqca-qt5.so.2
%attr(755,root,root) %{_libdir}/libqca-qt5.so.*.*
%dir %{_libdir}/qt5/plugins/crypto
%attr(755,root,root) %{_libdir}/qt5/plugins/crypto/libqca-cyrus-sasl.so
%attr(755,root,root) %{_libdir}/qt5/plugins/crypto/libqca-gcrypt.so
%attr(755,root,root) %{_libdir}/qt5/plugins/crypto/libqca-gnupg.so
%attr(755,root,root) %{_libdir}/qt5/plugins/crypto/libqca-logger.so
%attr(755,root,root) %{_libdir}/qt5/plugins/crypto/libqca-nss.so
%attr(755,root,root) %{_libdir}/qt5/plugins/crypto/libqca-ossl.so
%attr(755,root,root) %{_libdir}/qt5/plugins/crypto/libqca-softstore.so
%{_mandir}/man1/qcatool-qt5.1*

%files -n qca-qt5-devel
%defattr(644,root,root,755)
%{_includedir}/qt5/Qca-qt5
%{_libdir}/cmake/Qca-qt5
%attr(755,root,root) %{_libdir}/libqca-qt5.so
%{_pkgconfigdir}/qca2-qt5.pc
%{_libdir}/qt5/mkspecs/features/crypto.prf
