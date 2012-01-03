# revision 19440
# category Package
# catalog-ctan /macros/latex/contrib/chessfss
# catalog-date 2008-08-17 13:56:26 +0200
# catalog-license lppl
# catalog-version 1.2a
Name:		texlive-chessfss
Version:	1.2a
Release:	2
Summary:	A package to handle chess fonts
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/chessfss
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/chessfss.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/chessfss.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/chessfss.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This package offers commands to use and switch between chess
fonts. It uses the LaTeX font selection scheme (nfss). The
package doesn't parse, format and print PGN input like e.g. the
packages skak or texmate; the aim of the package is to offer
writers of chess packages a bundle of commands for fonts, so
that they don't have to implement all these commands for
themselves. A normal user can use the package to print e.g.
single chess symbols and simple diagrams. The documentation
contains also a section about installation of chess fonts.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/fonts/enc/dvips/chessfss/chess-board-example-enc.enc
%{_texmfdistdir}/fonts/enc/dvips/chessfss/chess-fig-example-enc.enc
%{_texmfdistdir}/tex/latex/chessfss/chessfss.sty
%{_texmfdistdir}/tex/latex/chessfss/lsb1enc.def
%{_texmfdistdir}/tex/latex/chessfss/lsb1skak.fd
%{_texmfdistdir}/tex/latex/chessfss/lsb1skaknew.fd
%{_texmfdistdir}/tex/latex/chessfss/lsb2enc.def
%{_texmfdistdir}/tex/latex/chessfss/lsb2skak.fd
%{_texmfdistdir}/tex/latex/chessfss/lsb2skaknew.fd
%{_texmfdistdir}/tex/latex/chessfss/lsb3enc.def
%{_texmfdistdir}/tex/latex/chessfss/lsb3skak.fd
%{_texmfdistdir}/tex/latex/chessfss/lsb3skaknew.fd
%{_texmfdistdir}/tex/latex/chessfss/lsbc1enc.def
%{_texmfdistdir}/tex/latex/chessfss/lsbc1skaknew.fd
%{_texmfdistdir}/tex/latex/chessfss/lsbc2enc.def
%{_texmfdistdir}/tex/latex/chessfss/lsbc2skaknew.fd
%{_texmfdistdir}/tex/latex/chessfss/lsbc3enc.def
%{_texmfdistdir}/tex/latex/chessfss/lsbc3skaknew.fd
%{_texmfdistdir}/tex/latex/chessfss/lsbc4enc.def
%{_texmfdistdir}/tex/latex/chessfss/lsbc4skaknew.fd
%{_texmfdistdir}/tex/latex/chessfss/lsbc5enc.def
%{_texmfdistdir}/tex/latex/chessfss/lsbc5skaknew.fd
%{_texmfdistdir}/tex/latex/chessfss/lsbenc.def
%{_texmfdistdir}/tex/latex/chessfss/lsbskak.fd
%{_texmfdistdir}/tex/latex/chessfss/lsbskaknew.fd
%{_texmfdistdir}/tex/latex/chessfss/lsfenc.def
%{_texmfdistdir}/tex/latex/chessfss/lsfskak.fd
%{_texmfdistdir}/tex/latex/chessfss/lsfskaknew.fd
%{_texmfdistdir}/tex/latex/chessfss/lsienc.def
%{_texmfdistdir}/tex/latex/chessfss/lsiskak.fd
%{_texmfdistdir}/tex/latex/chessfss/lsiskaknew.fd
%doc %{_texmfdistdir}/doc/latex/chessfss/README
%doc %{_texmfdistdir}/doc/latex/chessfss/README.TEXLIVE
#- source
%doc %{_texmfdistdir}/source/latex/chessfss/chessfss-src.dtx
%doc %{_texmfdistdir}/source/latex/chessfss/chessfss.ins

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar fonts tex doc source %{buildroot}%{_texmfdistdir}
