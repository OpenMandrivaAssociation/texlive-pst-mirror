# revision 32997
# category Package
# catalog-ctan /graphics/pstricks/contrib/pst-mirror
# catalog-date 2014-02-26 23:03:13 +0100
# catalog-license lppl
# catalog-version 1.01
Name:		texlive-pst-mirror
Version:	1.01
Release:	3
Summary:	Images on a spherical mirror
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/graphics/pstricks/contrib/pst-mirror
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/pst-mirror.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/pst-mirror.doc.tar.xz
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
%doc %{_texmfdistdir}/doc/generic/pst-mirror/createEPS/make.sh
%doc %{_texmfdistdir}/doc/generic/pst-mirror/createEPS/script.readme
%doc %{_texmfdistdir}/doc/generic/pst-mirror/createEPS/scripts/filtre.pl
%doc %{_texmfdistdir}/doc/generic/pst-mirror/createEPS/test.pdf
%doc %{_texmfdistdir}/doc/generic/pst-mirror/createEPS/test.sh
%doc %{_texmfdistdir}/doc/generic/pst-mirror/createEPS/test.tex
%doc %{_texmfdistdir}/doc/generic/pst-mirror/createEPS/xa.eps
%doc %{_texmfdistdir}/doc/generic/pst-mirror/createEPS/xa.tex
%doc %{_texmfdistdir}/doc/generic/pst-mirror/createEPS/xb.eps
%doc %{_texmfdistdir}/doc/generic/pst-mirror/createEPS/xc.eps
%doc %{_texmfdistdir}/doc/generic/pst-mirror/pst-mirror-doc.bib
%doc %{_texmfdistdir}/doc/generic/pst-mirror/pst-mirror-doc.pdf
%doc %{_texmfdistdir}/doc/generic/pst-mirror/pst-mirror-doc.tex

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar dvips tex doc %{buildroot}%{_texmfdistdir}
