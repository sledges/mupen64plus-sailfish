Name:		mupen64plus
#BuildArch:	armv7hl
Version:	2.0
Release:	1%{?dist}
Summary:	Nintendo 64 Emulator

Group:		Emulators
License:	GPLv2
URL:		http://code.google.com/p/mupen64plus
Source0:	%{name}-%{version}.tar.bz2

BuildRequires:	bash
#BuildRequires:	gcc-c++
BuildRequires:	boost-devel
BuildRequires:	pkgconfig(libpng)
BuildRequires:	pkgconfig(glesv2)
BuildRequires:	pkgconfig(sdl2)
BuildRequires:	pkgconfig(zlib)
BuildRequires:  pkgconfig(audioresource)
BuildRequires:  pkgconfig(glib-2.0)

%description
Mupen64plus is a cross-platform plugin bases N64 emulator
which is capable of accurately playing many games.

%prep
%setup -q

%build
cd mupen64plus-audio-sdl
PREFIX=%{_prefix} make all -C projects/unix
cd ..
cd mupen64plus-core
PREFIX=%{_prefix} USE_GLES=1 OSD=0 NEON=1 make all -C projects/unix
cd ..
cd mupen64plus-input-sdl
PREFIX=%{_prefix} make all -C projects/unix
cd ..
cd mupen64plus-input-sdltouch
PREFIX=%{_prefix} make all -C projects/unix
cd ..
cd mupen64plus-rsp-hle
PREFIX=%{_prefix} make all -C projects/unix
cd ..
cd mupen64plus-ui-console
PREFIX=%{_prefix} make all -C projects/unix
cd ..
cd mupen64plus-video-glide64mk2
PREFIX=%{_prefix} NO_SSE=1 USE_GLES=1 make all -C projects/unix
cd ..

%install
mkdir -p %{buildroot}/usr/lib/mupen64plus
cd mupen64plus-audio-sdl
PREFIX=%{_prefix} make install -C projects/unix
cd ..
cd mupen64plus-core
PREFIX=%{_prefix} USE_GLES=1 OSD=0 NEON=1 make install -C projects/unix
cd ..
cd mupen64plus-input-sdl
PREFIX=%{_prefix} make install -C projects/unix
cd ..
cd mupen64plus-input-sdltouch
PREFIX=%{_prefix} make install -C projects/unix
cd ..
cd mupen64plus-rsp-hle
PREFIX=%{_prefix} make install -C projects/unix
cd ..
cd mupen64plus-ui-console
PREFIX=%{_prefix} make install -C projects/unix
cd ..
cd mupen64plus-video-glide64mk2
PREFIX=%{_prefix} NO_SSE=1 USE_GLES=1 make install -C projects/unix
cd ..

%clean
cd mupen64plus-audio-sdl
PREFIX=%{_prefix} make clean -C projects/unix
cd ..
cd mupen64plus-core
PREFIX=%{_prefix} USE_GLES=1 OSD=0 NEON=1 make clean -C projects/unix
cd ..
cd mupen64plus-input-sdl
PREFIX=%{_prefix} make clean -C projects/unix
cd ..
cd mupen64plus-input-sdltouch
PREFIX=%{_prefix} make clean -C projects/unix
cd ..
cd mupen64plus-rsp-hle
PREFIX=%{_prefix} make clean -C projects/unix
cd ..
cd mupen64plus-ui-console
PREFIX=%{_prefix} make clean -C projects/unix
cd ..
cd mupen64plus-video-glide64mk2
PREFIX=%{_prefix} NO_SSE=1 USE_GLES=1 make clean -C projects/unix
cd ..

%post
/sbin/ldconfig -n %{_libdir}/mupen64plus

%postun
/sbin/ldconfig -n %{_libdir}/mupen64plus

%files
%defattr(-,root,root,-)
%{_bindir}/%{name}
%{_libdir}/mupen64plus/mupen64plus-audio-sdl.so
%{_libdir}/libmupen64plus.so.*
%{_datadir}/mupen64plus/font.ttf
%{_datadir}/mupen64plus/mupen64plus.ini
%{_datadir}/mupen64plus/mupencheat.txt
%{_includedir}/mupen64plus/m64p_*.h
%{_libdir}/mupen64plus/mupen64plus-input-sdl.so
%{_datadir}/mupen64plus/InputAutoCfg.ini
%{_libdir}/mupen64plus/mupen64plus-input-sdltouch.so
%{_libdir}/mupen64plus/mupen64plus-rsp-hle.so
%{_libdir}/mupen64plus/mupen64plus-video-glide64mk2.so
%{_datadir}/mupen64plus/Glide64mk2.ini

%changelog
* Sat Dec 27 2014 Franz-Josef Haider <f_haider@gmx.at> - 2.0-1
- Initial package 
