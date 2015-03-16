# Description #
A collection of general-purpose commandline scripts for editing and analyzing data stored in tab-delimited files. Advanced functionality can be achieved by "piping" the output of commands together. Several other utilities written for various scientific purposes are also available.


---


# Installation #
Installation for Unix/Linux systems (including Mac OS X) is simple:
  1. Download the compressed tarball here: http://code.google.com/p/ihms-science/source/browse/ihms-science.tar.bz2
  1. Uncompress the directory, and place it anywhere you'd like.
  1. Modify your shell's $PATH variable by adding the following line to your ".cshrc" or ".bash\_profile" file in your home directory (replacing "`/path/to/ihms-science`" with the actual path to the ihms-science directory of course):

> Bash:
`PATH=$PATH:/path/to/ihms-science; export PATH`
> > T-shell (or C-shell, etc.):
`set path=( $path /path/to/ihms-science )`


---


# Documentation #

## The "[tab](tab.md)" suite ##

> These Perl scripts are for the modification of tab or other character delimited data files. By using tab scripts "piped" together, mathematical operations can be successively applied on a per-row or column basis:

> <b><code>&amp;&gt;tread -col 1 input.dat | tmath -f subtract 10 | tsmooth -exp 0.5 | twrite -col 1 output.dat</code></b>


## The "[saxs](saxs.md)" suite ##
> This collection of scripts ease processing and analyzing small angle x-ray scattering (SAXS) data. Many of them work closely with the well-known [ATSAS](http://www.embl-hamburg.de/biosaxs/software.html) SAXS analysis software.

  * <b>saxsplot</b> - rapidly generates scattering profile plots in [xmgrace](http://plasma-gate.weizmann.ac.il/Grace/)

  * <b>gnom_rmax</b> - aids users in correctly determining the proper R<sub>max</sub> values for their data. Generates I(0), R<sub>g</sub> , and chi-squared plots to the experimental data at a range of R<sub>max</sub> values.

  * <b>damn</b> - automatically generates multiple DAMMIN/GASBOR scattering envelopes with provided data
## [Miscellaneous](Documentation.md) apps ##
> Other scripts that I've found useful and or necessary to write at some time or another. These include atomic coordinate extraction from [Gaussian](http://www.gaussian.com/) output logs to retrieving experimental conditions from isothermal titration calorimetry datafiles.

> See the [Documentation](Documentation.md) for a full list.