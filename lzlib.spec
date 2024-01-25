%define dont_remove_libtool_files 1
%define major 1
%define libname %mklibname lz %{major}
%define develname %mklibname lz -d

Name:		lzlib
Summary:	A compression library for lzip files
Version:	1.14
Release:	1
License:	GPLv3+
Group:		System/Libraries
URL:		http://www.nongnu.org/lzip/lzlib.html
Source0:	http://download.savannah.gnu.org/releases/lzip/lzlib/lzlib-%{version}.tar.lz
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
Summary:	A compression library for lzip files
Group:		System/Libraries

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
Summary:	A compression library for lzip files
Group:		Development/C
Requires:	%{libname} = %{version}
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

#------------------------------------------------------------------------------

%prep
%autosetup -p1

%build
%configure --enable-shared
sed -i -e 's|^CC =.*|CC = %{__cc}|;s|^CFLAGS =.*|CFLAGS = %{optflags}|;s|^LDFLAGS =.*|LDFLAGS = %{ldflags}|' Makefile
%make_build

%install
%make_install

%check
%make check
