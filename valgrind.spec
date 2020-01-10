%{?scl:%scl_package valgrind}

Summary: Tool for finding memory management bugs in programs
Name: %{?scl_prefix}valgrind
Version: 3.8.1
Release: 3.7%{?dist}
Epoch: 1
License: GPLv2
URL: http://www.valgrind.org/
Group: Development/Debuggers

# Only necessary for RHEL, will be ignored on Fedora
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Source0: http://www.valgrind.org/downloads/valgrind-%{version}.tar.bz2

Patch1: valgrind-3.8.1-cachegrind-improvements.patch

# KDE#307103 - sys_openat If pathname is absolute, then dirfd is ignored.
Patch2: valgrind-3.8.1-openat.patch

# KDE#211352 - helgrind races in helgrind's own mythread_wrapper
Patch3: valgrind-3.8.1-helgrind-race-supp.patch

Patch4: valgrind-3.8.1-stat_h.patch

# Support really ancient gcc. Check __GNUC__ >= 3 for __builtin_expect.
Patch5: valgrind-3.8.1-config_h.patch

# KDE#307101 - sys_capget second argument can be NULL 
Patch6: valgrind-3.8.1-capget.patch

# KDE#263034 - Crash when loading some PPC64 binaries 
Patch7: valgrind-3.8.1-pie.patch

# configure detection change from armv7* to armv[57]*.
Patch8: valgrind-3.8.1-enable-armv5.patch

Patch9: valgrind-3.8.1-ldso-supp.patch

# On x86 GCC 4.6 and later now defaults to -fomit-frame-pointer
# together with emitting unwind info (-fasynchronous-unwind-tables).
# So, try CF info first.
# RHEL 6.4 has GCC 4.4.6, so disable.
#Patch10: valgrind-3.8.1-x86-backtrace.patch

# KDE#305431 - Use find_buildid shdr fallback for separate .debug files
Patch11: valgrind-3.8.1-find-buildid.patch

# KDE#305513 - Robustify abbrev reading (part already upstream).
Patch12: valgrind-3.8.1-abbrev-parsing.patch

# KDE#307038 - DWARF2 CFI reader: unhandled DW_OP_ opcode 0x8 (DW_OP_const1u) 
Patch13: valgrind-3.8.1-cfi_dw_ops.patch

# On some ppc64 installs these test just hangs
Patch14: valgrind-3.8.1-gdbserver_tests-mcinvoke-ppc64.patch

# KDE#307285 - x86_amd64 feature test for avx in test suite is wrong
# Should test OSXSAVE first before executing XGETBV.
Patch15: valgrind-3.8.1-x86_amd64_features-avx.patch

# KDE#307155 - gdbserver_tests/filter_gdb should filter out syscall-template.S
# This is only a real issue when glibc-debuginfo is installed.
Patch16: valgrind-3.8.1-gdbserver_tests-syscall-template-source.patch

# KDE#307290 - memcheck overlap testcase needs memcpy version filter
Patch17: valgrind-3.8.1-overlap_memcpy_filter.patch
# Note: Need to make memcheck/tests/filter_memcpy executable

# KDE#307729 - pkgconfig support broken valgrind.pc
# valt_load_address=@VALT_LOAD_ADDRESS@
Patch18: valgrind-3.8.1-pkg-config.patch

# KDE#253519 - Memcheck reports auxv pointer accesses as invalid reads. 
Patch19: valgrind-3.8.1-proc-auxv.patch

# KDE#307828 - SSE optimized wcscpy, wcscmp, wcsrchr and wcschr trigger
# uninitialised value and/or invalid read warnings
Patch20: valgrind-3.8.1-wcs.patch

# KDE#305728 - Add support for AVX2, BMI1, BMI2 and FMA instructions 
# Combined patch for:
# - valgrind-avx2-1.patch
# - valgrind-avx2-2.patch
# - valgrind-avx2-3.patch
# - valgrind-avx2-4.patch
# - valgrind-bmi-1.patch
# - valgrind-bmi-2.patch
# - valgrind-bmi-3.patch
# - valgrind-fma-1.patch
# - valgrind-memcheck-avx2-bmi-fma.patch
# - valgrind-vmaskmov-load.patch
# - valgrind-avx2-5.patch
# - valgrind-bmi-4.patch
# - valgrind-avx2-bmi-fma-tests.tar.bz2
#
# NOTE: Need to touch empty files from tar file:
# ./none/tests/amd64/avx2-1.stderr.exp
# ./none/tests/amd64/fma.stderr.exp
# ./none/tests/amd64/bmi.stderr.exp
Patch21: valgrind-3.8.1-avx2-bmi-fma.patch.gz
# Small fixup for above patch, just a configure check.
# This is equivalent to valgrind-bmi-5.patch from KDE#305728
Patch22: valgrind-3.8.1-bmi-conf-check.patch
# Partial backport of upstream revision 12884 without it AVX2 VPBROADCASTB
# insn is broken under memcheck.
Patch23: valgrind-3.8.1-memcheck-mc_translate-Iop_8HLto16.patch
# vgtest files should prereq that the binary is there (for old binutils).
Patch24: valgrind-3.8.1-avx2-prereq.patch

# KDE#308321 - testsuite memcheck filter interferes with gdb_filter
Patch25: valgrind-3.8.1-filter_gdb.patch

# KDE#308341 - vgdb should report process exit (or fatal signal) 
Patch26: valgrind-3.8.1-gdbserver_exit.patch

# KDE#164485 - VG_N_SEGNAMES and VG_N_SEGMENTS are (still) too small
Patch27: valgrind-3.8.1-aspacemgr_VG_N_SEGs.patch

# KDE#308427 - s390 memcheck reports tsearch conditional jump or move
#              depends on uninitialized value [workaround, suppression]
Patch28: valgrind-3.8.1-s390_tsearch_supp.patch

# KDE#307106 - unhandled instruction bytes: f0 0f c0 02 (lock xadd)
Patch29: valgrind-3.8.1-xaddb.patch

# KDE#323713 Support mmxext (integer sse) subset on i386 (athlon)
Patch30: valgrind-3.8.1-mmxext.patch

# KDE#310931 message-security assist instruction extension not implemented 
Patch31: valgrind-3.8.1-s390-STFLE.patch

# KDE#321969 - Support [lf]setxattr on ppc32 and ppc64 linux kernel
Patch32: valgrind-3.8.1-ppc-setxattr.patch

# KDE#316503 Implement SSE4 MOVNTDQA insn.
Patch33: valgrind-3.8.1-movntdqa.patch

# KDE#280114 AMD64 general protection fail reported in signal handler
Patch34: valgrind-3.8.1-amd64-sigstack.patch

# KDE#318643 annotate_trace_memory tests go into infinite loop on arm and ppc
Patch35: valgrind-3.8.1-annotate-trace-memory.patch

# KDE#331337 - s390x WARNING: unhandled syscall: 326 (dup3)
Patch36: valgrind-3.8.1-s390-dup3.patch

# KDE#311407 - ssse3 bcopy (actually converted memcpy) causes invalid read
Patch37: valgrind-3.8.1-bcopy.patch

# KDE#308089 - Enable prctl on ppc64-linux.
Patch38: valgrind-3.8.1-ppc64-prctl.patch

Obsoletes: valgrind-callgrind
%ifarch x86_64 ppc64
# Ensure glibc{,-devel} is installed for both multilib arches
BuildRequires: /lib/libc.so.6 /usr/lib/libc.so /lib64/libc.so.6 /usr/lib64/libc.so
%endif
%if 0%{?fedora} >= 15
BuildRequires: glibc-devel >= 2.14
%else
%if 0%{?rhel} >= 6
BuildRequires: glibc-devel >= 2.12
%else
BuildRequires: glibc-devel >= 2.5
%endif
%endif
%ifarch %{ix86} x86_64 ppc ppc64
BuildRequires: openmpi-devel >= 1.3.3
%endif

# For %%build and %%check.
# In case of a software collection, pick the matching gdb and binutils.
BuildRequires: %{?scl_prefix}gdb
BuildRequires: %{?scl_prefix}binutils

%{?scl:Requires:%scl_runtime}

ExclusiveArch: %{ix86} x86_64 ppc ppc64 s390x %{arm}
%ifarch %{ix86}
%define valarch x86
%define valsecarch %{nil}
%endif
%ifarch x86_64
%define valarch amd64
%define valsecarch x86
%endif
%ifarch ppc
%define valarch ppc32
%define valsecarch ppc64
%endif
%ifarch ppc64
%define valarch ppc64
%define valsecarch ppc32
%endif
%ifarch s390x
%define valarch s390x
%define valsecarch %{nil}
%endif
%ifarch armv7hl
%define valarch armv7hl
%define valsecarch %{nil}
%endif
%ifarch armv5tel
%define valarch armv5tel
%define valsecarch %{nil}
%endif

# Disable build root strip policy
%define __spec_install_post /usr/lib/rpm/brp-compress || :

# Disable -debuginfo package generation
%define debug_package	%{nil}

%description
Valgrind is a tool to help you find memory-management problems in your
programs. When a program is run under Valgrind's supervision, all
reads and writes of memory are checked, and calls to
malloc/new/free/delete are intercepted. As a result, Valgrind can
detect a lot of problems that are otherwise very hard to
find/diagnose.

%package devel
Summary: Development files for valgrind
Group: Development/Debuggers
Requires: %{?scl_prefix}valgrind = %{epoch}:%{version}-%{release}

%description devel
Header files and libraries for development of valgrind aware programs
or valgrind plugins.

%package openmpi
Summary: OpenMPI support for valgrind
Group: Development/Debuggers
Requires: %{?scl_prefix}valgrind = %{epoch}:%{version}-%{release}

%description openmpi
A wrapper library for debugging OpenMPI parallel programs with valgrind.
See file:///usr/share/doc/%{?scl_prefix}valgrind-%{version}/html/mc-manual.html#mc-manual.mpiwrap
for details.

%prep
%setup -q %{?scl:-n %{pkg_name}-%{version}}

%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1
%patch6 -p1
%patch7 -p1
%patch8 -p1
%patch9 -p1
#%patch10 -p1
%patch11 -p1
%patch12 -p1
%patch13 -p1
%patch14 -p1
%patch15 -p1
%patch16 -p1
%patch17 -p1
chmod 755 memcheck/tests/filter_memcpy
%patch18 -p1
%patch19 -p1
%patch20 -p1

# Add support for AVX2, BMI1, BMI2 and FMA instructions
%patch21 -p1
touch ./none/tests/amd64/avx2-1.stderr.exp
touch ./none/tests/amd64/fma.stderr.exp
touch ./none/tests/amd64/bmi.stderr.exp
%patch22 -p1
%patch23 -p1
%patch24 -p1

%patch25 -p1
%patch26 -p1
%patch27 -p1
%ifarch s390x
%patch28 -p1
%endif

%patch29 -p1

%patch30 -p1
%patch31 -p1
%patch32 -p1
%patch33 -p1
%patch34 -p1
%patch35 -p1
%patch36 -p1
%patch37 -p1
%patch38 -p1

# To suppress eventual automake warnings/errors
rm -f gdbserver_tests/filter_gdb.orig

%build
# We need to use the software collection compiler and binutils if available.
# The configure checks might otherwise miss support for various newer
# assembler instructions.
%{?scl:PATH=%{_bindir}${PATH:+:${PATH}}}

CC=gcc
%ifarch x86_64 ppc64
# Ugly hack - libgcc 32-bit package might not be installed
mkdir -p libgcc/32
ar r libgcc/32/libgcc_s.a
ar r libgcc/libgcc_s_32.a
CC="gcc -B `pwd`/libgcc/"
%endif

# Old openmpi-devel has version depended paths for mpicc.
%if 0%{?fedora} >= 13 || 0%{?rhel} >= 6
%define mpiccpath %{!?scl:%{_libdir}}%{?scl:%{_root_libdir}}/openmpi/bin/mpicc
%else
%define mpiccpath %{!?scl:%{_libdir}}%{?scl:%{_root_libdir}}/openmpi/*/bin/mpicc
%endif

# Filter out some flags that cause lots of valgrind test failures.
# Also filter away -O2, valgrind adds it wherever suitable, but
# not for tests which should be -O0, as they aren't meant to be
# compiled with -O2 unless explicitely requested.
OPTFLAGS="`echo " %{optflags} " | sed 's/ -m\(64\|3[21]\) / /g;s/ -fexceptions / /g;s/ -fstack-protector / / g;s/ -Wp,-D_FORTIFY_SOURCE=2 / /g;s/ -O2 / /g;s/^ //;s/ $//'`"
%configure CC="$CC" CFLAGS="$OPTFLAGS" CXXFLAGS="$OPTFLAGS" \
%ifarch %{ix86} x86_64 ppc ppc64
  --with-mpicc=%{mpiccpath} \
%endif
  GDB=%{_bindir}/gdb

make %{?_smp_mflags}

# Ensure there are no unexpected file descriptors open,
# the testsuite otherwise fails.
cat > close_fds.c <<EOF
#include <stdlib.h>
#include <unistd.h>
int main (int argc, char *const argv[])
{
  int i, j = sysconf (_SC_OPEN_MAX);
  if (j < 0)
    exit (1);
  for (i = 3; i < j; ++i)
    close (i);
  execvp (argv[1], argv + 1);
  exit (1);
}
EOF
gcc $RPM_OPT_FLAGS -o close_fds close_fds.c

# XXX pth_cancel2 hangs on x86_64
echo 'int main (void) { return 0; }' > none/tests/pth_cancel2.c

%install
rm -rf $RPM_BUILD_ROOT
make DESTDIR=$RPM_BUILD_ROOT install
mkdir docs.installed
mv $RPM_BUILD_ROOT%{_datadir}/doc/valgrind/* docs.installed/
rm -f docs.installed/*.ps

%if "%{valsecarch}" != ""
pushd $RPM_BUILD_ROOT%{_libdir}/valgrind/
rm -f *-%{valsecarch}-* || :
for i in *-%{valarch}-*; do
  j=`echo $i | sed 's/-%{valarch}-/-%{valsecarch}-/'`
%ifarch ppc
  ln -sf ../../lib64/valgrind/$j $j
%else
  ln -sf ../../lib/valgrind/$j $j
%endif
done
popd
%endif

rm -f $RPM_BUILD_ROOT%{_libdir}/valgrind/*.supp.in

%ifarch %{ix86} x86_64
# To avoid multilib clashes in between i?86 and x86_64,
# tweak installed <valgrind/config.h> a little bit.
for i in HAVE_PTHREAD_CREATE_GLIBC_2_0 \
%if 0%{?rhel} == 5
         HAVE_BUILTIN_ATOMIC HAVE_BUILTIN_ATOMIC_CXX \
%endif
         ; do
  sed -i -e 's,^\(#define '$i' 1\|/\* #undef '$i' \*/\)$,#ifdef __x86_64__\n# define '$i' 1\n#endif,' \
    $RPM_BUILD_ROOT%{_includedir}/valgrind/config.h
done
%endif

%check
# Build the test files with the software collection compiler if available.
%{?scl:PATH=%{_bindir}${PATH:+:${PATH}}}
make %{?_smp_mflags} check || :
echo ===============TESTING===================
./close_fds make regtest || :
# Make sure test failures show up in build.log
# Gather up the diffs (at most the first 20 lines for each one)
MAX_LINES=20
diff_files=`find . -name '*.diff' | sort`
if [ z"$diff_files" = z ] ; then
   echo "Congratulations, all tests passed!" >> diffs
else
   for i in $diff_files ; do
      echo "=================================================" >> diffs
      echo $i                                                  >> diffs
      echo "=================================================" >> diffs
      if [ `wc -l < $i` -le $MAX_LINES ] ; then
         cat $i                                                >> diffs
      else
         head -n $MAX_LINES $i                                 >> diffs
         echo "<truncated beyond $MAX_LINES lines>"            >> diffs
      fi
   done
fi
cat diffs
echo ===============END TESTING===============

%files
%defattr(-,root,root)
%doc COPYING NEWS README_*
%doc docs.installed/html docs.installed/*.pdf
%{_bindir}/*
%dir %{_libdir}/valgrind
%{_libdir}/valgrind/*[^ao]
%{_libdir}/valgrind/[^l]*o
%{_mandir}/man1/*

%files devel
%defattr(-,root,root)
%{_includedir}/valgrind
%dir %{_libdir}/valgrind
%{_libdir}/valgrind/*.a
%{_libdir}/pkgconfig/*

%ifarch %{ix86} x86_64 ppc ppc64
%files openmpi
%defattr(-,root,root)
%dir %{_libdir}/valgrind
%{_libdir}/valgrind/libmpiwrap*.so
%endif

%changelog
* Mon Aug 11 2014 Mark Wielaard <mjw@redhat.com> 3.8.1-3.7
- Add valgrind-3.8.1-ppc64-prctl.patch. (#1126483)

* Wed Jul 16 2014 Mark Wielaard <mjw@redhat.com> 3.8.1-3.6
- Add valgrind-3.8.1-bcopy.patch. (#1120021)

* Tue May 27 2014 Mark Wielaard <mjw@redhat.com> 3.8.1-3.5
- Add valgrind-3.9.0-s390-dup3.patch. (#1101422)

* Fri May 23 2014 Mark Wielaard <mjw@redhat.com> 3.8.1-3.4
- Add valgrind-3.8.1-annotate-trace-memory.patch (#1100645)

* Fri May 09 2014 Mark Wielaard <mjw@redhat.com> 3.8.1-3.3
- Add valgrind-3.8.1-mmxext.patch (#828341)
- Add valgrind-3.8.1-s390-STFLE.patch (#881893)
  s390 message-security assist (MSA) instruction extension not implemented.
- Add valgrind-3.8.1-ppc-setxattr.patch (#1007400)
- Implement SSE4 MOVNTDQA insn (valgrind-3.8.1-movntdqa.patch) (#1012932)
- Add valgrind-3.8.1-amd64-sigstack.patch (#1024162)

* Tue Oct 16 2012 Mark Wielaard <mjw@redhat.com> 3.8.1-3.2
- Add valgrind-3.8.1-xaddb.patch (#866941, KDE#307106)

* Mon Oct 15 2012 Mark Wielaard <mjw@redhat.com> 3.8.1-3.1
- Rebase on fedora valgrind 3.8.1-3 (#823005,#816244,#862795,#730303)

* Fri Sep 21 2012 Mark Wielaard <mjw@redhat.com> 3.8.1-2.1
- Rebase on fedora valgrind 3.8.1-2 (#823005)

* Mon Mar  5 2012 Jakub Jelinek <jakub@redhat.com> 3.6.0-5
- improve POWER7 support (#739143)
- handle memalign requests up to 4MB alignment instead of 1MB (#757728)

* Tue Aug  2 2011 Jakub Jelinek <jakub@redhat.com> 3.6.0-4
- don't fail if s390x support patch hasn't been applied,
  move testing into %%check (#708522)
- POWER7 support (#694598)
- handle REX.W form of FXSAVE (#713956, KDE#194402)
- workaround redundant REX.W prefix for PTEST in JITed code
  (#713956, KDE#279071)
- avoid redundant test in ppc backports (#717218, KDE#279062)

* Thu Feb 24 2011 Dodji Seketeli <dodji@redhat.com> - 1:3.6.0-3
- Fix libvex_guest_offsets.h wrapper for ix86
- Add a new one for ppc/ppc64

* Wed Feb 23 2011  <dodji@redhat.com> - 1:3.6.0-2
- fix PIE handling on ppc/ppc64 (#665289)
- hook in pwrite64 syscall on ppc64 (#679906)
- Add a wrapper header for libvex_guest_offsets.h to allow // installs
  on x86_64 an x*86 arches.

* Fri Nov 12 2010 Jakub Jelinek <jakub@redhat.com> 3.6.0-1
- update to 3.6.0
- add s390x support (#632354)
- provide a replacement for str{,n}casecmp{,_l} (#626470)

* Tue May 18 2010 Jakub Jelinek <jakub@redhat.com> 3.5.0-18
- rebuilt against glibc 2.12

* Mon Apr 12 2010 Jakub Jelinek <jakub@redhat.com> 3.5.0-16
- change pub_tool_basics.h not to include config.h (#579283)
- add valgrind-openmpi package for OpenMPI support (#565541)
- allow NULL second argument to capget (#450976)

* Wed Apr  7 2010 Jakub Jelinek <jakub@redhat.com> 3.5.0-15
- handle i686 nopw insns with more than one data16 prefix (#574889)
- DWARF4 support
- handle getcpu and splice syscalls

* Wed Jan 20 2010 Jakub Jelinek <jakub@redhat.com> 3.5.0-14
- fix build against latest glibc headers

* Wed Jan 20 2010 Jakub Jelinek <jakub@redhat.com> 3.5.0-13
- DW_OP_mod is unsigned modulus instead of signed
- fix up valgrind.pc (#551277)

* Mon Dec 21 2009 Jakub Jelinek <jakub@redhat.com> 3.5.0-12
- don't require offset field to be set in adjtimex's
  ADJ_OFFSET_SS_READ mode (#545866)

* Wed Dec  2 2009 Jakub Jelinek <jakub@redhat.com> 3.5.0-10
- add handling of a bunch of recent syscalls and fix some
  other syscall wrappers (Dodji Seketeli)
- handle prelink created split of .bss into .dynbss and .bss
  and similarly for .sbss and .sdynbss (#539874)

* Wed Nov  4 2009 Jakub Jelinek <jakub@redhat.com> 3.5.0-9
- rebuilt against glibc 2.11
- use upstream version of the ifunc support

* Wed Oct 28 2009 Jakub Jelinek <jakub@redhat.com> 3.5.0-8
- add preadv/pwritev syscall support

* Tue Oct 27 2009 Jakub Jelinek <jakub@redhat.com> 3.5.0-7
- add perf_counter_open syscall support (#531271)
- add handling of some sbb/adc insn forms on x86_64 (KDE#211410)

* Fri Oct 23 2009 Jakub Jelinek <jakub@redhat.com> 3.5.0-6
- ppc and ppc64 fixes

* Thu Oct 22 2009 Jakub Jelinek <jakub@redhat.com> 3.5.0-5
- add emulation of 0x67 prefixed loop* insns on x86_64 (#530165)

* Wed Oct 21 2009 Jakub Jelinek <jakub@redhat.com> 3.5.0-4
- handle reading of .debug_frame in addition to .eh_frame
- ignore unknown DWARF3 expressions in evaluate_trivial_GX
- suppress helgrind race errors in helgrind's own mythread_wrapper
- fix compilation of x86 tests on x86_64 and ppc tests

* Wed Oct 14 2009 Jakub Jelinek <jakub@redhat.com> 3.5.0-3
- handle many more DW_OP_* ops that GCC now uses
- handle the more compact form of DW_AT_data_member_location
- don't strip .debug_loc etc. from valgrind binaries

* Mon Oct 12 2009 Jakub Jelinek <jakub@redhat.com> 3.5.0-2
- add STT_GNU_IFUNC support (Dodji Seketeli, #518247)
- wrap inotify_init1 syscall (Dodji Seketeli, #527198)
- fix mmap/mprotect handling in memcheck (KDE#210268)

* Fri Aug 21 2009 Jakub Jelinek <jakub@redhat.com> 3.5.0-1
- update to 3.5.0

* Tue Jul 28 2009 Jakub Jelinek <jakub@redhat.com> 3.4.1-7
- handle futex ops newly added during last 4 years (#512121)

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> 3.4.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Mon Jul 13 2009 Jakub Jelinek <jakub@redhat.com> 3.4.1-5
- add support for DW_CFA_{remember,restore}_state

* Mon Jul 13 2009 Jakub Jelinek <jakub@redhat.com> 3.4.1-4
- handle version 3 .debug_frame, .eh_frame, .debug_info and
  .debug_line (#509197)

* Mon May 11 2009 Jakub Jelinek <jakub@redhat.com> 3.4.1-3
- rebuilt against glibc 2.10.1

* Wed Apr 22 2009 Jakub Jelinek <jakub@redhat.com> 3.4.1-2
- redirect x86_64 ld.so strlen early (#495645)

* Mon Mar  9 2009 Jakub Jelinek <jakub@redhat.com> 3.4.1-1
- update to 3.4.1

* Tue Feb  9 2009 Jakub Jelinek <jakub@redhat.com> 3.4.0-3
- update to 3.4.0

* Wed Apr 16 2008 Jakub Jelinek <jakub@redhat.com> 3.3.0-3
- add suppressions for glibc 2.8
- add a bunch of syscall wrappers (#441709)

* Mon Mar  3 2008 Jakub Jelinek <jakub@redhat.com> 3.3.0-2
- add _dl_start suppression for ppc/ppc64

* Mon Mar  3 2008 Jakub Jelinek <jakub@redhat.com> 3.3.0-1
- update to 3.3.0
- split off devel bits into valgrind-devel subpackage

* Thu Oct 18 2007 Jakub Jelinek <jakub@redhat.com> 3.2.3-7
- add suppressions for glibc >= 2.7

* Fri Aug 31 2007 Jakub Jelinek <jakub@redhat.com> 3.2.3-6
- handle new x86_64 nops (#256801, KDE#148447)
- add support for private futexes (KDE#146781)
- update License tag

* Fri Aug  3 2007 Jakub Jelinek <jakub@redhat.com> 3.2.3-5
- add ppc64-linux symlink in valgrind ppc.rpm, so that when
  rpm prefers 32-bit binaries over 64-bit ones 32-bit
  /usr/bin/valgrind can find 64-bit valgrind helper binaries
  (#249773)
- power5+ and power6 support (#240762)

* Thu Jun 28 2007 Jakub Jelinek <jakub@redhat.com> 3.2.3-4
- pass GDB=%{_prefix}/gdb to configure to fix default
  --db-command (#220840)

* Wed Jun 27 2007 Jakub Jelinek <jakub@redhat.com> 3.2.3-3
- add suppressions for glibc >= 2.6
- avoid valgrind internal error if io_destroy syscall is
  passed a bogus argument

* Tue Feb 13 2007 Jakub Jelinek <jakub@redhat.com> 3.2.3-2
- fix valgrind.pc again

* Tue Feb 13 2007 Jakub Jelinek <jakub@redhat.com> 3.2.3-1
- update to 3.2.3

* Wed Nov  8 2006 Jakub Jelinek <jakub@redhat.com> 3.2.1-7
- some cachegrind improvements (Ulrich Drepper)

* Mon Nov  6 2006 Jakub Jelinek <jakub@redhat.com> 3.2.1-6
- fix valgrind.pc (#213149)
- handle Intel Core2 cache sizes in cachegrind (Ulrich Drepper)

* Wed Oct 25 2006 Jakub Jelinek <jakub@redhat.com> 3.2.1-5
- fix valgrind on ppc/ppc64 where PAGESIZE is 64K (#211598)

* Sun Oct  1 2006 Jakub Jelinek <jakub@redhat.com> 3.2.1-4
- adjust for glibc-2.5

* Wed Sep 27 2006 Jakub Jelinek <jakub@redhat.com> 3.2.1-3
- another DW_CFA_set_loc handling fix

* Tue Sep 26 2006 Jakub Jelinek <jakub@redhat.com> 3.2.1-2
- fix openat handling (#208097)
- fix DW_CFA_set_loc handling

* Tue Sep 19 2006 Jakub Jelinek <jakub@redhat.com> 3.2.1-1
- update to 3.2.1 bugfix release
  - SSE3 emulation fixes, reduce memcheck false positive rate,
    4 dozens of bugfixes

* Mon Aug 21 2006 Jakub Jelinek <jakub@redhat.com> 3.2.0-5
- handle the new i686/x86_64 nops (#203273)

* Fri Jul 28 2006 Jeremy Katz <katzj@redhat.com> - 1:3.2.0-4
- rebuild to bring ppc back

* Wed Jul 12 2006 Jesse Keating <jkeating@redhat.com> - 1:3.2.0-3.1
- rebuild

* Fri Jun 16 2006 Jakub Jelinek <jakub@redhat.com> 3.2.0-3
- handle [sg]et_robust_list syscall on ppc{32,64}

* Fri Jun 16 2006 Jakub Jelinek <jakub@redhat.com> 3.2.0-2
- fix ppc64 symlink to 32-bit valgrind libdir
- handle a few extra ppc64 syscalls

* Thu Jun 15 2006 Jakub Jelinek <jakub@redhat.com> 3.2.0-1
- update to 3.2.0
  - ppc64 support

* Fri May 26 2006 Jakub Jelinek <jakub@redhat.com> 3.1.1-3
- handle [sg]et_robust_list syscalls on i?86/x86_64
- handle *at syscalls on ppc
- ensure on x86_64 both 32-bit and 64-bit glibc{,-devel} are
  installed in the buildroot (#191820)

* Wed Apr 12 2006 Jakub Jelinek <jakub@redhat.com> 3.1.1-2
- handle many syscalls that were unhandled before, especially on ppc

* Mon Apr  3 2006 Jakub Jelinek <jakub@redhat.com> 3.1.1-1
- upgrade to 3.1.1
  - many bugfixes

* Mon Mar 13 2006 Jakub Jelinek <jakub@redhat.com> 3.1.0-2
- add support for DW_CFA_val_offset{,_sf}, DW_CFA_def_cfa_sf
  and skip over DW_CFA_val_expression quietly
- adjust libc/ld.so filenames in glibc-2.4.supp for glibc 2.4
  release

* Mon Jan  9 2006 Jakub Jelinek <jakub@redhat.com> 3.1.0-1
- upgrade to 3.1.0 (#174582)
  - many bugfixes, ppc32 support

* Thu Oct 13 2005 Jakub Jelinek <jakub@redhat.com> 3.0.1-2
- remove Obsoletes for valgrind-callgrind, as it has been
  ported to valgrind 3.0.x already

* Sun Sep 11 2005 Jakub Jelinek <jakub@redhat.com> 3.0.1-1
- upgrade to 3.0.1
  - many bugfixes
- handle xattr syscalls on x86-64 (Ulrich Drepper)

* Fri Aug 12 2005 Jakub Jelinek <jakub@redhat.com> 3.0.0-3
- fix amd64 handling of cwtd instruction
- fix amd64 handling of e.g. sarb $0x4,val(%rip)
- speedup amd64 insn decoding

* Fri Aug 12 2005 Jakub Jelinek <jakub@redhat.com> 3.0.0-2
- lower x86_64 stage2 base from 112TB down to 450GB, so that
  valgrind works even on 2.4.x kernels.  Still way better than
  1.75GB that stock valgrind allows

* Fri Aug 12 2005 Jakub Jelinek <jakub@redhat.com> 3.0.0-1
- upgrade to 3.0.0
  - x86_64 support
- temporarily obsolete valgrind-callgrind, as it has not been
  ported yet

* Tue Jul 12 2005 Jakub Jelinek <jakub@redhat.com> 2.4.0-3
- build some insn tests with -mmmx, -msse or -msse2 (#161572)
- handle glibc-2.3.90 the same way as 2.3.[0-5]

* Wed Mar 30 2005 Jakub Jelinek <jakub@redhat.com> 2.4.0-2
- resurrect the non-upstreamed part of valgrind_h patch
- remove 2.1.2-4G patch, seems to be upstreamed
- resurrect passing -fno-builtin in memcheck tests

* Sun Mar 27 2005 Colin Walters <walters@redhat.com> 2.4.0-1
- New upstream version 
- Update valgrind-2.2.0-regtest.patch to 2.4.0; required minor
  massaging
- Disable valgrind-2.1.2-4G.patch for now; Not going to touch this,
  and Fedora does not ship 4G kernel by default anymore
- Remove upstreamed valgrind-2.2.0.ioctls.patch
- Remove obsolete valgrind-2.2.0-warnings.patch; Code is no longer
  present
- Remove upstreamed valgrind-2.2.0-valgrind_h.patch
- Remove obsolete valgrind-2.2.0-unnest.patch and
  valgrind-2.0.0-pthread-stacksize.patch; valgrind no longer
  includes its own pthread library

* Thu Mar 17 2005 Jakub Jelinek <jakub@redhat.com> 2.2.0-10
- rebuilt with GCC 4

* Tue Feb  8 2005 Jakub Jelinek <jakub@redhat.com> 2.2.0-8
- avoid unnecessary use of nested functions for pthread_once
  cleanup

* Mon Dec  6 2004 Jakub Jelinek <jakub@redhat.com> 2.2.0-7
- update URL (#141873)

* Tue Nov 16 2004 Jakub Jelinek <jakub@redhat.com> 2.2.0-6
- act as if NVALGRIND is defined when using <valgrind.h>
  in non-m32/i386 programs (#138923)
- remove weak from VALGRIND_PRINTF*, make it static and
  add unused attribute

* Mon Nov  8 2004 Jakub Jelinek <jakub@redhat.com> 2.2.0-4
- fix a printout and possible problem with local variable
  usage around setjmp (#138254)

* Tue Oct  5 2004 Jakub Jelinek <jakub@redhat.com> 2.2.0-3
- remove workaround for buggy old makes (#134563)

* Fri Oct  1 2004 Jakub Jelinek <jakub@redhat.com> 2.2.0-2
- handle some more ioctls (Peter Jones, #131967)

* Thu Sep  2 2004 Jakub Jelinek <jakub@redhat.com> 2.2.0-1
- update to 2.2.0

* Thu Jul 22 2004 Jakub Jelinek <jakub@redhat.com> 2.1.2-3
- fix packaging of documentation

* Tue Jul 20 2004 Jakub Jelinek <jakub@redhat.com> 2.1.2-2
- allow tracing of 32-bit binaries on x86-64

* Tue Jul 20 2004 Jakub Jelinek <jakub@redhat.com> 2.1.2-1
- update to 2.1.2
- run make regtest as part of package build
- use glibc-2.3 suppressions instead of glibc-2.2 suppressions

* Thu Apr 29 2004 Colin Walters <walters@redhat.com> 2.0.0-1
- update to 2.0.0

* Tue Feb 25 2003 Jeff Johnson <jbj@redhat.com> 1.9.4-0.20030228
- update to 1.9.4 from CVS.
- dwarf patch from Graydon Hoare.
- sysinfo patch from Graydon Hoare, take 1.

* Fri Feb 14 2003 Jeff Johnson <jbj@redhat.com> 1.9.3-6.20030207
- add return codes to syscalls.
- fix: set errno after syscalls.

* Tue Feb 11 2003 Graydon Hoare <graydon@redhat.com> 1.9.3-5.20030207
- add handling for separate debug info (+fix).
- handle blocking readv/writev correctly.
- comment out 4 overly zealous pthread checks.

* Tue Feb 11 2003 Jeff Johnson <jbj@redhat.com> 1.9.3-4.20030207
- move _pthread_desc to vg_include.h.
- implement pthread_mutex_timedlock().
- implement pthread_barrier_wait().

* Mon Feb 10 2003 Jeff Johnson <jbj@redhat.com> 1.9.3-3.20030207
- import all(afaik) missing functionality from linuxthreads.

* Sun Feb  9 2003 Jeff Johnson <jbj@redhat.com> 1.9.3-2.20030207
- import more missing functionality from linuxthreads in glibc-2.3.1.

* Sat Feb  8 2003 Jeff Johnson <jbj@redhat.com> 1.9.3-1.20030207
- start fixing nptl test cases.

* Fri Feb  7 2003 Jeff Johnson <jbj@redhat.com> 1.9.3-0.20030207
- build against current 1.9.3 with nptl hacks.

* Tue Oct 15 2002 Alexander Larsson <alexl@redhat.com>
- Update to 1.0.4

* Fri Aug  9 2002 Alexander Larsson <alexl@redhat.com>
- Update to 1.0.0

* Wed Jul  3 2002 Alexander Larsson <alexl@redhat.com>
- Update to pre4.

* Tue Jun 18 2002 Alexander Larsson <alla@lysator.liu.se>
- Add threadkeys and extra suppressions patches. Bump epoch.

* Mon Jun 17 2002 Alexander Larsson <alla@lysator.liu.se>
- Updated to 1.0pre1

* Tue May 28 2002 Alex Larsson <alexl@redhat.com>
- Updated to 20020524. Added GLIBC_PRIVATE patch

* Thu May  9 2002 Jonathan Blandford <jrb@redhat.com>
- add missing symbol __pthread_clock_settime

* Wed May  8 2002 Alex Larsson <alexl@redhat.com>
- Update to 20020508

* Mon May  6 2002 Alex Larsson <alexl@redhat.com>
- Update to 20020503b

* Thu May  2 2002 Alex Larsson <alexl@redhat.com>
- update to new snapshot

* Mon Apr 29 2002 Alex Larsson <alexl@redhat.com> 20020428-1
- update to new snapshot

* Fri Apr 26 2002 Jeremy Katz <katzj@redhat.com> 20020426-1
- update to new snapshot

* Thu Apr 25 2002 Alex Larsson <alexl@redhat.com> 20020424-5
- Added stack patch. Commented out other patches.

* Wed Apr 24 2002 Nalin Dahyabhai <nalin@redhat.com> 20020424-4
- filter out GLIBC_PRIVATE requires, add preload patch

* Wed Apr 24 2002 Alex Larsson <alexl@redhat.com> 20020424-3
- Make glibc 2.2 and XFree86 4 the default supressions

* Wed Apr 24 2002 Alex Larsson <alexl@redhat.com> 20020424-2
- Added patch that includes atomic.h

* Wed Apr 24 2002 Alex Larsson <alexl@redhat.com> 20020424-1
- Initial build
