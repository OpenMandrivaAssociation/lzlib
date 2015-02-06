%define dont_remove_libtool_files 1
%define major 1
%define libname %mklibname lz %major
%define develname %mklibname lz -d
%define staticname %mklibname lz -d -s

Name:		lzlib
Summary:	A compression library for lzip files
Version:	1.3
Release:	3
License:	GPLv3+
Group:		System/Libraries
URL:		http://www.nongnu.org/lzip/lzlib.html
Source0:	http://download.savannah.gnu.org/releases/lzip/%{name}-%{version}.tar.lz
BuildRequires:	lzip

%description
The lzlib compression library provides in-memory LZMA compression
and decompression functions, including integrity checking
of the decompressed data. The compressed data format used by the library
is the lzip format.

Lzlib implements a simplified version of the LZMA (Lempel-Ziv-Markov
chain-Algorithm) algorithm. The original LZMA algorithm was designed by Igor
Pavlov. For a description of the LZMA algorithm, see the lzip manual. 

#------------------------------------------------------------------------------

%package -n %{libname}
Summary:        A compression library for lzip files
Group:          System/Libraries

%description -n %{libname}
The lzlib compression library provides in-memory LZMA compression
and decompression functions, including integrity checking
of the decompressed data. The compressed data format used by the library
is the lzip format.

Lzlib implements a simplified version of the LZMA (Lempel-Ziv-Markov
chain-Algorithm) algorithm. The original LZMA algorithm was designed by Igor
Pavlov. For a description of the LZMA algorithm, see the lzip manual.

%files -n %{libname}
%{_libdir}/*.so.%{major}*

#------------------------------------------------------------------------------

%package -n %{develname}
Summary:        A compression library for lzip files
Group:          Development/C
Requires:       %{libname} = %{version}
Provides:	%{name}-devel = %{EVRD}

%description -n %{develname}
The lzlib compression library provides in-memory LZMA compression
and decompression functions, including integrity checking
of the decompressed data. The compressed data format used by the library
is the lzip format.

Lzlib implements a simplified version of the LZMA (Lempel-Ziv-Markov
chain-Algorithm) algorithm. The original LZMA algorithm was designed by Igor
Pavlov. For a description of the LZMA algorithm, see the lzip manual.

%files -n %{develname}
%{_libdir}/*.so
%{_infodir}/*
%{_includedir}/*
%doc AUTHORS ChangeLog NEWS README

%if %{mdvver} < 201200
%post -n %{develname}
%_install_info

%postun -n %{develname}
%_remove_install_info
%endif

#------------------------------------------------------------------------------

%package -n %{staticname}
Summary:	A compression library for lzip files
Group:		Development/C

%description -n %{staticname}
The lzlib compression library provides in-memory LZMA compression
and decompression functions, including integrity checking
of the decompressed data. The compressed data format used by the library
is the lzip format.

Lzlib implements a simplified version of the LZMA (Lempel-Ziv-Markov
chain-Algorithm) algorithm. The original LZMA algorithm was designed by Igor
Pavlov. For a description of the LZMA algorithm, see the lzip manual.

%files -n %{staticname}
%{_libdir}/*.a

#------------------------------------------------------------------------------

%prep
%setup -q

%build
%configure --enable-shared
%make

%install
%makeinstall_std
pushd %{buildroot}%{_libdir}/
ln -s liblz.so.%{major} liblz.so
popd

%check
make check


%changelog
* Tue Apr 10 2012 Dmitry Mikhirev <dmikhirev@mandriva.org> 1.3-2
+ Revision: 790244
- update to 1.3
- run make check after build

* Tue Mar 13 2012 Dmitry Mikhirev <dmikhirev@mandriva.org> 1.2-2
+ Revision: 784542
- fix symlink in devel package

* Mon Mar 12 2012 Dmitry Mikhirev <dmikhirev@mandriva.org> 1.2-1
+ Revision: 784427
- BR fixed
- fix devel provides
- imported package lzlib

