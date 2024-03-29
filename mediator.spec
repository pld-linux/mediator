# 
# Note: RPMS should be placed in contrib/supported dirs on ftp site
#
Summary:	Mediator - SQL backend for your xbase/clipper applications
Summary(pl.UTF-8):	Mediator - Backend SQL dla aplikacji xbase/clipper
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
URL:		http://www.otc.pl/
ExclusiveArch:	%{ix86}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Mediator enables porting any Delphi, CA-Clipper, CA-Visual Objects or
(x)Harbour application to the relational database environment, which
in practice means the end of problems with damaged indexes, too large
tables or unsatisfactory data protection.

%description -l pl.UTF-8
Mediator umożliwia przeniesienie dowolnej aplikacji Delphi, CA-Clipper
lub Harbour do środowiska relacyjnej bazy danych, co oznacza koniec
problemów z uszkodzonymi indeksami, zbyt dużymi tabelami czy
niedostateczną ochroną.

%package client
Summary:	Mediator client
Summary(pl.UTF-8):	Klient Mediatora
Group:		Applications

%description client 
This is Linux-based client for Mediator. These files are useful if you
develop xbase/xharbour/clipper code on Linux platform. They are not
needed for running normal server. 

%description client -l pl.UTF-8
To jest oparty na Linuksie klient Mediatora. Pliki te są użyteczne do
rozwijania oprogramowania xbase/xharbour/clipper pracującego na
platformie linuksowej. Ten pakiet nie jest konieczny aby uruchomić
zwykły serwer.

%package mysql
Summary:	Mediator for MySQL
Summary(pl.UTF-8):	Mediator dla MySQL-a
Group:		Applications

%description mysql
Mediator server for MySQL.

%description mysql -l pl.UTF-8
Serwer Mediatora dla MySQL-a.

%package postgresql 
Summary:	Mediator for PostgreSQL
Summary(pl.UTF-8):	Mediator dla PostgreSQL-a
Group:		Applications

%description postgresql
Mediator server for PostgreSQL.

%description postgresql -l pl.UTF-8
Serwer Mediatora dla PostgreSQL-a.

%prep
%setup -q -c

%build
mkdir pgsql
cd pgsql
tar xfz %{SOURCE2}
cd ..

mkdir mysql
cd mysql
tar xfz %{SOURCE1}
cd ..

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{/var/lib/mediator,%{_bindir}}
install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}/{hb,xhb}

#cp -avR medcl/ %_datadir/{%name} ???

install pgsql/mediator $RPM_BUILD_ROOT%{_bindir}/mediator-pgsql
install mysql/mediator $RPM_BUILD_ROOT%{_bindir}/mediator-mysql

install medcl/hb/source/sample/medntx/*.prg $RPM_BUILD_ROOT%{_examplesdir}/%{name}/hb
install medcl/xhb/source/sample/medntx/*.prg $RPM_BUILD_ROOT%{_examplesdir}/%{name}/xhb

%clean
rm -rf $RPM_BUILD_ROOT

# XXX: Don't remove licence file from main package!
%files
%defattr(644,root,root,755)
%doc medcl/doc/licencja.txt

%files client
%doc medcl/doc/{Progd42.pdf,Progd42e.pdf,instcllx.txt,instcllxpl.txt}
%dir %{_examplesdir}/%{name}
%dir %{_examplesdir}/%{name}/hb
%dir %{_examplesdir}/%{name}/xhb
%{_examplesdir}/%{name}/hb/*.prg
%{_examplesdir}/%{name}/xhb/*.prg

%files mysql
%defattr(644,root,root,755)
%doc mysql/msvmsqlxpl.txt
%attr(755,root,root) %{_bindir}/mediator-mysql

%files postgresql
%defattr(644,root,root,755)
%doc pgsql/msvpsqlxpl.txt
%attr(755,root,root) %{_bindir}/mediator-pgsql
