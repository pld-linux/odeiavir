Summary:	This is OdeiaVir, a program that, well, hates viruses
Summary(pl):	OdeiaVir - program, który nienawidzi wirusów
Name:		odeiavir
Version:	0.5.0pre5
Release:	0
License:	GPL
Group:		Applications/Mail
Vendor:		Juan Carlos Castro y Castro <jcastro@vialink.com.br>
Source0:	http://virus.isverybad.org/%{name}-%{version}.tar.gz
# Source0-md5:	843f88d43c03352e71278d928fc9a2f0
Patch0:		%{name}-opt.patch
URL:		http://virus.isverybad.org/
Requires:	qmail
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
It is meant to be placed at the local delivery phase of the e-mail
message lifetime. It currently works reliably only with qmail, but
there is embrionary (as in pre-alpha, extremely-untested) Sendmail
support. You call it from the user's .qmail file. This means you can
virus-proof ezmlm lists, too, with ease. Sendmail users will have to
change the Mlocal line in sendmail.cf.

%description -l pl
OdeiaVir jest pomy¶lany tak, by byæ umieszczony na etapie lokalnego
dostarczania wiadomo¶ci e-mail. Aktualnie dzia³a wiarygodnie tylko z
qmailem, ale jest pocz±tkowa (pre-alpha, ekstremalnie nie testowana)
obs³uga sendmaila. Program mo¿e byæ wywo³any z pliku .qmail
u¿ytkownika. Oznacza to, ¿e mo¿na ³atwo zabezpieczyæ przed wirusami
listy mailowe ezmlm. U¿ytkownicy sendmaila bêd± musieli zmieniæ
liniê Mlocal w pliku sendmail.cf.

%prep
%setup -q
%patch -p1

%build
%{__make} \
	CC="%{__cc}" \
	OPT="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_mandir}/man8,%{_sysconfdir}/%{name}}

install odeiavir  $RPM_BUILD_ROOT%{_bindir}/odeiavir
install odeiavir.8 $RPM_BUILD_ROOT%{_mandir}/man8
install config warning.txt $RPM_BUILD_ROOT%{_sysconfdir}/%{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog README TODO scripts *.txt FAQ
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man8/*
%config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/*
