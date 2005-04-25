# 
# Note: RPMS should be placed in contrib/supported dirs on ftp site
#
Summary:	Mediator - SQL backend for your xbase/clipper applications
Summary(pl):	Mediator - Backend SQL dla Twoiich aplikacji xbase/clipper
Name:		mediator
Version:	4222
Release:	0.1
Epoch:		0
License:	Commercial (Full 5 user licence for free - registration may be required)
Group:		Applications
# client:
Source0:	http://www.otc.pl/download/files_pl/mcl/medclhbpl.tar.gz
# pgsql:
Source2:	http://www.otc.pl/download/files_pl/mpg/msvpsqlx.tgz
# mysql:
Source1:	http://www.otc.pl/download/files_pl/mmysql/msvmsqlx.tgz

#Source3:	http://www.otc.pl/download/files_pl/mpg/PGSQL_INSTALL_PL.TXT
#Source4:	http://www.otc.pl/download/files_pl/mpg/PGSQL_INSTALL_EN.TXT
#Source5:	http://www.otc.pl/download/files_pl/mcl/instcllxpl.txt
#Source6:	http://www.otc.pl/download/files_pl/mmysql/MYSQL_INSTALL_PL.TXT
#Source7:	http://www.otc.pl/download/files_pl/mmysql/MYSQL_INSTALL_EN.TXT
URL:		http://www.otc.pl
ExclusiveArch:	%{ix86}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Mediator enables porting any Delphi, CA-Clipper, CA-Visual Objects or
(x)Harbour application to the relational database environment, which
in practice means the end of problems with damaged indexes, too large
tables or unsatisfactory data protection.

%description -l pl
Mediator umo¿liwia przeniesienie dowolnej aplikacji Delphi, CA-Clipper
lub Harbour do ¶rodowiska relacyjnej bazy danych, co oznacza koniec
problemów z uszkodzonymi indeksami, zbyt du¿ymi tablicami czy
niedostateczn± ochron±.

#%package client #Summary: mediator client #Summary(pl): Klient
mediatora #Group: -

#%description subpackage

#%description subpackage -l pl

%package mysql
Summary:	mediator dla mysql
Summary(pl):	Mediator dla mysqla
Group:		Applications

%description mysql
Mediator for mysql

%description mysql -l pl
Mediator dla mysql

%package postgresql 
Summary: mediator for postgres 
Summary(pl): Mediator dla postgresa 
Group: Applications

%description postgresql
Mediator for postgres

%description postgresql -l pl
Mediator dla postgresa

%prep
%setup -q -c -n %{name}

%build

mkdir pgsql
cd pgsql
tar xfvz %{SOURCE2}
cd ..

mkdir mysql
cd mysql
tar xfvz %{SOURCE1}
cd ..

%install
rm -rf $RPM_BUILD_ROOT
# create directories if necessary
install -d $RPM_BUILD_ROOT{/var/lib/mediator,%{_bindir}}

install pgsql/mediator $RPM_BUILD_ROOT%{_bindir}/mediator-pgsql
install mysql/mediator $RPM_BUILD_ROOT%{_bindir}/mediator-mysql

%clean
rm -rf $RPM_BUILD_ROOT

%pre

%post

%preun

%postun

%files
%defattr(644,root,root,755)
#%doc pgsql/msvpsqlxpl.txt mysql/msvmsqlxpl.txt

#%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/*

#%attr(755,root,root) %{_bindir}/*

#%{_datadir}/%{name}

# initscript and its config
#%attr(754,root,root) /etc/rc.d/init.d/%{name}
#%config(noreplace) %verify(not md5 mtime size) /etc/sysconfig/%{name}

%files mysql
%defattr(644,root,root,755)
%doc mysql/msvmsqlxpl.txt
%attr(755,root,root) %{_bindir}/mediator-mysql

%files postgresql
%defattr(644,root,root,755)
%doc pgsql/msvpsqlxpl.txt
%attr(755,root,root) %{_bindir}/mediator-pgsql
