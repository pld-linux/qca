# TODO:
# - fix chrpath
#
# chrpath stripping fails
%define	no_install_post_chrpath	1
Summary:	Qt Cryptographic Architecture (QCA) Library
Summary(pl.UTF-8):	Biblioteka Qt Cryptographic Architecture (QCA)
Name:		qca
Version:	2.0.0
Release:	1
License:	LGPL v2.1
Group:		Libraries
Source0:	http://delta.affinix.com/download/qca/2.0/%{name}-%{version}.tar.bz2
# Source0-md5:	07d54358ef4880d05b3c6f56b629aa55
URL:		http://delta.affinix.com/qca/
BuildRequires:	QtCore-devel
BuildRequires:	QtNetwork-devel
BuildRequires:	QtTest-devel
BuildRequires:	libstdc++-devel
BuildRequires:	openssl-devel >= 0.9.7d
BuildRequires:	qt4-qmake
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

%build
export QTDIR=%{_prefix}
export LIBDIR=%{_libdir}

./configure \
	--prefix=%{_prefix} \
	--libdir=%{_libdir} \
	--datadir=%{_datadir}

# probably could be done but breaks the build now:
#
#qmake %{name}.pro \
#	QMAKE_CXX="%{__cxx}" \
#	QMAKE_LINK="%{__cxx}" \
#	QMAKE_CXXFLAGS_RELEASE="%{rpmcflags}" \
#	QMAKE_RPATH=

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_pkgconfigdir}

%{__make} install \
	INSTALL_ROOT=$RPM_BUILD_ROOT

install lib/*.pc $RPM_BUILD_ROOT%{_pkgconfigdir}
rm -rf  $RPM_BUILD_ROOT%{_prefix}/lib/pkgconfig

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc README
%attr(755,root,root) %{_bindir}/*
%attr(755,root,root) %{_libdir}/*.so.*
%{_mandir}/man1/*.1*
%{_datadir}/qca

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/*.so
%{_includedir}/QtCrypto
%{_pkgconfigdir}/*.pc
%{_libdir}/libqca.prl
%{_datadir}/qt4/mkspecs/features/crypto.prf
