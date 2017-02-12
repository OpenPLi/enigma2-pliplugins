AC_INIT([enigma2-pli-plugins],[0.0.1],[forum@openpli.org])
AM_INIT_AUTOMAKE([foreign])
AM_PATH_PYTHON()
AC_SUBST(LIBDIR)
AC_PATH_PROG(MSGFMT, msgfmt, AC_MSG_ERROR(Could not find msgfmt))

AC_ARG_WITH(po,
	AS_HELP_STRING([--with-po],[enable updating of po files]),
	[with_po="$withval"],[with_po="no"])
if test "$with_po" = "yes"; then
	AC_PATH_PROG(MSGINIT, msginit)
	AC_PATH_PROG(MSGMERGE, msgmerge)
	AC_PATH_PROG(MSGUNIQ, msguniq)
	AC_PATH_PROG(XGETTEXT, xgettext)
	if test -z "$MSGINIT" -o -z "$MSGMERGE" -o -z "$MSGUNIQ" -o -z "$XGETTEXT"; then
		AC_MSG_ERROR([Could not find required gettext tools])
	fi
fi
AM_CONDITIONAL(UPDATE_PO, test "$with_po" = "yes")

AC_OUTPUT([
Makefile
Extensions/Makefile
Extensions/UShare/Makefile
Extensions/OpenUitzendingGemist/Makefile
])
