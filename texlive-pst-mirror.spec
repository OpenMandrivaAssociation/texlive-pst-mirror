# revision 16370
# category Package
# catalog-ctan /graphics/pstricks/contrib/pst-mirror
# catalog-date 2009-12-14 16:47:24 +0100
# catalog-license lppl
# catalog-version 1.00
Name:		texlive-pst-mirror
Version:	1.00
Release:	2
Summary:	Images on a spherical mirror
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/graphics/pstricks/contrib/pst-mirror
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/pst-mirror.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/pst-mirror.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/pst-mirror.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package provides commands and supporting PostScript
material for drawing images as if reflected by a spherical
mirror.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/dvips/pst-mirror/pst-mirror.pro
%{_texmfdistdir}/tex/generic/pst-mirror/pst-mirror.tex
%{_texmfdistdir}/tex/latex/pst-mirror/pst-mirror.sty
%doc %{_texmfdistdir}/doc/generic/pst-mirror/Changes
%doc %{_texmfdistdir}/doc/generic/pst-mirror/README
%doc %{_texmfdistdir}/doc/generic/pst-mirror/pst-mirror-doc.bib
%doc %{_texmfdistdir}/doc/generic/pst-mirror/pst-mirror-doc.pdf
%doc %{_texmfdistdir}/doc/generic/pst-mirror/pst-mirror-doc.tex
#- source
%doc %{_texmfdistdir}/source/generic/pst-mirror/Makefile

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar dvips tex doc source %{buildroot}%{_texmfdistdir}
