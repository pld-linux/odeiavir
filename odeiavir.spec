Summary:	This is OdeiaVir, a program that, well, hates viruses
Summary(pl.UTF-8):	OdeiaVir - program, który nienawidzi wirusów
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

%description -l pl.UTF-8
OdeiaVir jest pomyślany tak, by być umieszczony na etapie lokalnego
dostarczania wiadomości e-mail. Aktualnie działa wiarygodnie tylko z
qmailem, ale jest początkowa (pre-alpha, ekstremalnie nie testowana)
obsługa sendmaila. Program może być wywołany z pliku .qmail
użytkownika. Oznacza to, że można łatwo zabezpieczyć przed wirusami
listy mailowe ezmlm. Użytkownicy sendmaila będą musieli zmienić linię
Mlocal w pliku sendmail.cf.

%prep
%setup -q
%patch -P0 -p1

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
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/*
