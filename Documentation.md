# Documentation for the following programs: #
  * [tab](tab.md) - separate page
  * [saxs](saxs.md) - separate page
  * [gnarl](gnarl.md) - separate page

  * [chisq\_col](Documentation#chisq_col.md)
  * [comma2tab](Documentation#comma2tab.md)
  * [gextract](Documentation#gextract.md)
  * [itcparse](Documentation#itcparse.md)
  * [makeattr](Documentation#makeattr.md)
  * [pdb2xyz](Documentation#pdb2xyz.md)
  * [psi2xyz](Documentation#psi2xyz.md)
  * [psiopt2xyz](Documentation#psiopt2xyz.md)
  * [stddev\_row](Documentation#stddev_row.md)
  * [tab2comma](Documentation#tab2comma.md)

# Notes #
  * Please see the [tab](tab.md), [saxs](saxs.md), and [gnarl](gnarl.md) pages for documentation on those applications.
  * Most programs and scripts contain built-in help. If run without arguments, or the -h argument, e.g. `itcparse -h`, a brief help should be provided
  * All of these programs are designed and verified to work with most linux distros and Macintosh OS X versions. Many use perl, and/or have dependencies on the [tab](tab.md) package. Please see the "requirements" section for each program.


---


# chisq\_col #
> ## Description: ##
> This script takes a tab-delimited dataset containing two (y1 y2) or three columns (x y1 y2) and calculates the SSE (sum squared of errors) or RSS (residual sum of squares) between the y1 and y2 columns.
> ## Usage: ##
> > `chisq_col -xyy|-yy (-log) [file]`

> ## Requirements: ##
> Expects that the [tab](tab.md) suite of programs be available in the environment's $PATH variable.


---


# comma2tab #
> ## Description: ##
> Hardly even a script, this is a classic tr "on-liner". It converts datasets in a comma-delimited format (e.g. 1,2,3) to tab-delimited e.g. (1   2   3)
> ## Usage: ##
> > `comma2tab in_file.csv out_file.dat`

> ## See also: ##
> [tab2comma](Documentation#tab2comma.md)


---


# gextract #
> ## Description: ##
> This app parses g03 or g09 [Gaussian](http://www.gaussian.com/) output files, extracting the xyz atomic coordinates. This is especially useful for watching the optimization of a molecule's geometry, e.g. with UCSF Chimera's [MD movie](http://www.cgl.ucsf.edu/chimera/docs/ContributedSoftware/movie/movie.html) ability.
> ## Usage: ##
> > `gextract [options] gaussian.log [output prefix]`
| option | function |
|:-------|:---------|
| `-n N` | Extract the structure at iteration N |
| `-l` | Extract only the last structure |
| `-r N1...N2` | Extract structures from iteration N1 to N2 |
| `+N1,N2,...` | Extract only specific structures (comma-delimited list) |

  * Note: if you wish to have gextract recognize atoms other than H,C,N,O,P, or S, add them to the first line of the program with any text editor.

> ## See also: ##
> [psi2xyz](Documentation#psi2xyz.md)
> [psiopt2xyz](Documentation#psiopt2xyz.md)


---


# itcparse #
> ## Description: ##
> Extracts the run-time parameters (reference power, stirring speed, injection volumes, etc.) from a .itc output file from a [Microcal](http://www.microcal.com/) ITC instrument. This program has been verified with the VP-ITC and iTC200 instruments.
> ## Usage: ##
> > `itcparse input.itc`

> or
> > `itcparse input.itc > parameters.dat`


---


# makeattr #

> ## Description: ##
> This utility generates a [UCSF Chimera](http://www.cgl.ucsf.edu/chimera/) attribute list, useful for setting structural model's attributes (e.g. color, depiction, etc.) on a per-residue (like a crystallographic b-factor, NMR hNOE ratio, etc.) basis.
> ## Usage: ##
> The input file is a tab-delimited file with two columns: the residue #, and a numeric value. This file is piped to makeattr.
  * Note: UCSF chimera assumes that attribute names beginning with a capital letter are abstract. See the Chimera [docs](http://www.cgl.ucsf.edu/chimera/docs/ContributedSoftware/defineattrib/defineattrib.html) for more info.
> > `cat input.dat | makeattr [options]`
| option | function |
|:-------|:---------|
| `-a` | attribute name |
| `-m` | match mode, e.g. `any,non-zero,1-to-1` |
| `-r` | recipient, e.g. `atoms,residues,moecules` |
| `-x` | atomspec prefix |
| `-y` | atomspec postfix |


---


# pdb2xyz #

> ## Description: ##
> Converts a pdb-format model file to an xyz-format file.
> ## Usage: ##
> > `pdb2xyz input.pdb > output.xyz`


---


# psi2xyz #

> ## Description: ##
> Extracts a single xyz-formatted structure file from a [Psi3](http://www.psicode.org/) output file. This is useful for verifying structure in a molecular viewer that doesn't understand connection matrices.
> ## Usage: ##
> > `pdb2xyz output.dat > output.xyz`

> ## See also: ##
> [psiopt2xyz](Documentation#psiopt2xyz.md)


---


# psiopt2xyz #
> ## Description: ##
> Similar to [gextract](Documentation#gextract.md), extracts molecular structure information (in an xyz format) for each step in a [Psi3](http://www.psicode.org/) structure optimization run. 
> ## Usage: ##
> > `psiopt2xyz (-last) output.dat`
| option | function |
|:-------|:---------|
| `-last` | extracts only the last structure |


---


# stddev\_row #

> ## Description: ##
> This script calculates the row-wise standard deviation from a tab-delimited (NXY) dataset. e.g. (X  y1   y2   y3...yN) . The file can contain any number of rows and columns.
> ## Usage: ##
> > `stddev_row input.dat`


---


# tab2comma #

> ## Description: ##
> Converts a tab-delimited (e.g. X   Y) dataset to a comma-delimited (e.g. X,Y) dataset.
> ## Usage: ##
> > `tab2comma input.dat output.csv`

> ## See also: ##
> [comma2tab](Documentation#comma2tab.md)