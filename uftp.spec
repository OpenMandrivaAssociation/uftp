%define name uftp
%define version 2.6.3
%define release %mkrel 2

Summary: A multicast FTP
Name: %{name}
Version: %{version}
Release: %{release}
Source0: %{name}.tar
License: GPL
Group: Networking/File transfer
Url: http://www.tcnj.edu/~bush/uftp.html
BuildRoot: %{_tmppath}/%{name}-buildroot

%description
UFTP is a multicast file transfer program, utilizing a protocol based on
Starburst MFTP. It is designed to reliably and efficiently transfer files
to multiple receivers simultaneously, where either the intended receivers
can be specified beforehand, or receivers can join the transfer when it is
initiated. This is useful for distributing large files to a large number of
receivers, and is especially useful for data distribution over a satellite
link (with two way communication), where the inherent delay makes any TCP
based communication terribly inefficient. UFTP has been used in the production
process of The Wall Street Journal to send WSJ pages over satellite to their
remote printing plants.

%package server
Summary: A multicast ftp server
Group: Networking/File transfer

%description server
UFTP is a multicast file transfer program, utilizing a protocol based on
Starburst MFTP. It is designed to reliably and efficiently transfer files
to multiple receivers simultaneously, where either the intended receivers
can be specified beforehand, or receivers can join the transfer when it is
initiated. This is useful for distributing large files to a large number of
receivers, and is especially useful for data distribution over a satellite
link (with two way communication), where the inherent delay makes any TCP
based communication terribly inefficient. UFTP has been used in the production
process of The Wall Street Journal to send WSJ pages over satellite to their
remote printing plants.

%prep
%setup -q -c

%build
%make -f makefile.linux CFLAGS="%optflags"

%install
rm -rf $RPM_BUILD_ROOT

mkdir -p %buildroot%_bindir
install -d %buildroot%_bindir
install -m 755 uftp %buildroot%_bindir/uftp
install -d %buildroot%_sbindir
install -m 755 uftpd %buildroot%_sbindir/uftpd
install -d %buildroot%_mandir/man1
install -m 644 uftp.1 %buildroot%_mandir/man1/uftp.1
install -m 644 uftpd.1 %buildroot%_mandir/man1/uftpd.1

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%_bindir/uftp
%_mandir/man1/uftp.1*
%doc Changes.txt ReadMe.txt

%files server
%defattr(-,root,root)
%_sbindir/uftpd
%_mandir/man1/uftpd.1*
%doc Changes.txt ReadMe.txt


%changelog
* Wed Sep 09 2009 Thierry Vignaud <tvignaud@mandriva.com> 2.6.3-2mdv2010.0
+ Revision: 434497
- rebuild

* Thu Sep 18 2008 Olivier Thauvin <nanardon@mandriva.org> 2.6.3-1mdv2009.0
+ Revision: 285637
- 2.6.3

  + Thierry Vignaud <tvignaud@mandriva.com>
    - rebuild

* Wed Jul 30 2008 Thierry Vignaud <tvignaud@mandriva.com> 2.6.1-3mdv2009.0
+ Revision: 255050
- rebuild

* Thu Feb 21 2008 Olivier Thauvin <nanardon@mandriva.org> 2.6.1-1mdv2008.1
+ Revision: 173678
- import uftp


