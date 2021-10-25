Summary:	Qt Cryptographic Architecture (QCA) Library
Summary(pl.UTF-8):	Biblioteka Qt Cryptographic Architecture (QCA)
Name:		qca
Version:	2.2.1
Release:	2
License:	LGPL v2.1
Group:		Libraries
Source0:	https://download.kde.org/stable/qca/%{version}/%{name}-%{version}.tar.xz
# Source0-md5:	5d809bf0ade891dc89dfd7639cbeaa9d
Patch0:		openssl3.patch
URL:		https://invent.kde.org/libraries/qca
BuildRequires:	QtCore-devel
BuildRequires:	QtGui-devel
BuildRequires:	QtNetwork-devel
BuildRequires:	QtTest-devel
BuildRequires:	cmake >= 2.8.2
BuildRequires:	libstdc++-devel
BuildRequires:	nss-devel
BuildRequires:	openssl-devel >= 0.9.7d
BuildRequires:	pkcs11-helper-devel
BuildRequires:	qt4-build >= 4.3.3-3
BuildRequires:	qt4-qmake >= 4.3.3-3
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

%prep
%setup -q
%patch0 -p1

%build
install -d build
cd build
QC_CERTSTORE_PATH=/etc/certs/ca-certificates.crt; export QC_CERTSTORE_PATH
export CXXFLAGS="%{rpmcxxflags} -fpermissive"
%cmake \
	-DQCA_LIBRARY_INSTALL_DIR=%{_libdir} \
	-DQCA_FEATURE_INSTALL_DIR=%{_datadir}/qt4/mkspecs/features/ \
	-DQT4_BUILD=ON \
	..
%{__make}
cd ..

%install
rm -rf $RPM_BUILD_ROOT
%{__make} -C build install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun -p /sbin/ldconfig

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
%attr(755,root,root) %{_libdir}/qca/crypto/libqca-pkcs11.so
%attr(755,root,root) %{_libdir}/qca/crypto/libqca-softstore.so
%{_mandir}/man1/qcatool.1*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libqca.so
%{_includedir}/QtCrypto
%{_pkgconfigdir}/qca2.pc
%{_datadir}/qt4/mkspecs/features/crypto.prf
%{_libdir}/cmake/Qca
