"""
Histogram - Create a histogram
"""
from pygmt.clib import Session
from pygmt.helpers import build_arg_string, fmt_docstring, kwargs_to_strings, use_alias


@fmt_docstring
@use_alias(
    A="horizontal",
    B="frame",
    C="cmap",
    D="annotate",
    E="barwidth",
    F="center",
    G="fill",
    J="projection",
    N="normal",
    Q="cumulative",
    R="region",
    S="step",
    T="series",
    W="pen",
    X="xshift",
    Y="yshift",
    Z="type",
    c="panel",
    l="label",
    p="perspective",
)
@kwargs_to_strings(R="sequence", T="sequence")
def histogram(self, table, **kwargs):
    r"""
    Plots a histogram, and can read data from a file or
    list, array, or dataframe.

    Full option list at :gmt-docs:`histogram.html`

    {aliases}

    Parameters
    ----------
    table : str, list, or 1d array
        A data file name, list, or 1d numpy array. This is a required argument.
    {J}
    {R}
    {B}
    {CPT}
    {G}
    {W}
    {c}
    annotate : bool or str
        [**+b**][**+f**\ *font*][**+o**\ *off*][**+r**]
        Annotate each bar with the count it represents.  Append any of the
        following modifiers: Use **+b** to place the labels beneath the bars
        instead of above; use **+f** to change to another font than the default
        annotation font; use **+o** to change the offset between bar and
        label [6p]; use **+r** to rotate the labels from horizontal to
        vertical.
    barwidth : int or float or str
        *width*\ [**+o**\ *offset*]
        Use an alternative histogram bar width than the default set via **-T**,
        and optionally shift all bars by an *offset*.  Here *width* is either
        an alternative width in data units, or the user may append a valid plot
        dimension unit (**c**\|\ **i**\|\ **p**) for a fixed dimension instead.
        Optionally, all bins may be shifted along the axis by *offset*. As for
        *width*, it may be given in data units of plot dimension units by
        appending the relevant unit.
    center : bool
        Center bin on each value. [Default is left edge].
    normal : bool or int or float or str
        [*mode*][**+p**\ *pen*]
        Draw the equivalent normal distribution; append desired
        pen [0.25p,black].
        The *mode* selects which central location and scale to use:

        * 0 = mean and standard deviation [Default];
        * 1 = median and L1 scale (1.4826 \* median absolute deviation; MAD);
        * 2 = LMS (least median of squares) mode and scale.

        The **-N** option may be repeated to draw several of these curves.
        **Note**: If **-w** is used then only *mode* = 0 is available and we
        will determine the parameters of the circular von Mises distribution
        instead.
    cumulative : bool or str
        [**r**]
        Draw a cumulative histogram. Append **r** to instead compute the
        reverse cumulative histogram.
    step : bool
        Draws a stairs-step diagram which does not include the internal bars
        of the default histogram.
    label : str
        Add a legend entry for the symbol or line being plotted.
    {p}
    horizontal : bool
        Plot the histogram using horizonal bars instead of the
        default vertical bars.
    series : int or str or list
        [*min*\ /*max*\ /]\ *inc*\ [**+n**\ ]
        Set the interval for the width of each bar in the histogram.
    {XY}
    type : int or str
        [*type*][**+w**]
        Choose between 6 types of histograms:

        * 0 = counts [Default]
        * 1 = frequency_percent
        * 2 = log (1.0 + count)
        * 3 = log (1.0 + frequency_percent)
        * 4 = log10 (1.0 + count)
        * 5 = log10 (1.0 + frequency_percent).

        To use weights provided as a second data column instead of pure counts,
        append **+w**.
    """
    kwargs = self._preprocess(**kwargs)  # pylint: disable=protected-access
    with Session() as lib:
        file_context = lib.virtualfile_from_data(check_kind="vector", data=table)
        with file_context as infile:
            arg_str = " ".join([infile, build_arg_string(kwargs)])
            lib.call_module("histogram", arg_str)
