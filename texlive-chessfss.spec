%global tl_name chessfss
%global tl_revision 79618

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.2a
Release:	%{tl_revision}.1
Summary:	A package to handle chess fonts
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/chessfss
License:	lppl1
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/chessfss.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/chessfss.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/chessfss.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This package offers commands to use and switch between chess fonts. It
uses the LaTeX font selection scheme (nfss). The package doesn't parse,
format and print PGN input like e.g. the packages skak or texmate; the
aim of the package is to offer writers of chess packages a bundle of
commands for fonts, so that they don't have to implement all these
commands for themselves. A normal user can use the package to print e.g.
single chess symbols and simple diagrams. The documentation contains
also a section about installation of chess fonts.

