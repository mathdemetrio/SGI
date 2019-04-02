import cairo
import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

from window import Window

SIZE = 10
xViewPortMax = 500
xViewPortMin = 0
yViewPortMax = 500
yViewPortMin = 0

tela = Window(xViewPortMin, yViewPortMin, xViewPortMax, yViewPortMax)

class Handler:
    def onDestroy(self, *args):
        Gtk.main_quit()


def onBtnPontoClicked(button):
    PontoWindow.show_all()


def transformadaViewPortCoordenadaX(x):
    auxiliar = (x - tela.getXMin()) / (tela.getXMax() - tela.getXMin())

    return auxiliar * (xViewPortMax - xViewPortMin)


def transformadaViewPortCoordenadaY(y):
    auxiliar = (y - tela.getYMin()) / (tela.getYMax() - tela.getYMin())

    return (1 - auxiliar) * (yViewPortMax - yViewPortMin)


def triangle(ctx):
    ctx.move_to(SIZE, 0)
    ctx.rel_line_to(SIZE, 2 * SIZE)
    ctx.rel_line_to(-2 * SIZE, 0)
    ctx.close_path()


def square(ctx):
    ctx.move_to(0, 0)
    ctx.rel_line_to(2 * SIZE, 0)
    ctx.rel_line_to(0, 2 * SIZE)
    ctx.rel_line_to(-2 * SIZE, 0)
    ctx.close_path()


def bowtie(ctx):
    ctx.move_to(0, 0)
    ctx.rel_line_to(2 * SIZE, 2 * SIZE)
    ctx.rel_line_to(-2 * SIZE, 0)
    ctx.rel_line_to(2 * SIZE, -2 * SIZE)
    ctx.close_path()


def inf(ctx):
    ctx.move_to(0, SIZE)
    ctx.rel_curve_to(0, SIZE, SIZE, SIZE, 2 * SIZE, 0)
    ctx.rel_curve_to(SIZE, -SIZE, 2 * SIZE, -SIZE, 2 * SIZE, 0)
    ctx.rel_curve_to(0, SIZE, -SIZE, SIZE, - 2 * SIZE, 0)
    ctx.rel_curve_to(-SIZE, -SIZE, - 2 * SIZE, -SIZE, - 2 * SIZE, 0)
    ctx.close_path()


def draw_shapes(ctx, x, y, fill):
    ctx.save()

    ctx.new_path()
    ctx.translate(x + SIZE, y + SIZE)
    bowtie(ctx)
    if fill:
        ctx.fill()
    else:
        ctx.stroke()

    ctx.new_path()
    ctx.translate(3 * SIZE, 0)
    square(ctx)
    if fill:
        ctx.fill()
    else:
        ctx.stroke()

    ctx.new_path()
    ctx.translate(3 * SIZE, 0)
    triangle(ctx)
    if fill:
        ctx.fill()
    else:
        ctx.stroke()

    ctx.new_path()
    ctx.translate(3 * SIZE, 0)
    inf(ctx)
    if fill:
        ctx.fill()
    else:
        ctx.stroke()

    ctx.restore()

def fill_shapes(ctx, x, y):
    draw_shapes(ctx, x, y, True)


def stroke_shapes(ctx, x, y):
    draw_shapes(ctx, x, y, False)


def draw(da, ctx):

    ctx.set_source_rgb(0, 0, 0)
    #ctx.scale(500, 500)

    larguraLinha = 2

    ctx.set_line_width(larguraLinha)
    ctx.set_line_cap(cairo.LINE_CAP_ROUND)
    #ctx.set_tolerance(0.1)

    x = transformadaViewPortCoordenadaX(50)
    y = transformadaViewPortCoordenadaY(50)
    ctx.move_to(x, y)
    ctx.line_to(x, y)
    ctx.stroke_preserve()

    # ctx.set_line_join(cairo.LINE_JOIN_ROUND)
    # ctx.set_dash([SIZE / 4.0, SIZE / 4.0], 0)
    # stroke_shapes(ctx, 0, 0)
    #
    # ctx.set_dash([], 0)
    # stroke_shapes(ctx, 0, 3 * SIZE)
    #
    # ctx.set_line_join(cairo.LINE_JOIN_BEVEL)
    # stroke_shapes(ctx, 0, 6 * SIZE)
    #
    # ctx.set_line_join(cairo.LINE_JOIN_MITER)
    # stroke_shapes(ctx, 0, 9 * SIZE)
    #
    # fill_shapes(ctx, 0, 12 * SIZE)
    #
    # ctx.set_line_join(cairo.LINE_JOIN_BEVEL)
    # fill_shapes(ctx, 0, 15 * SIZE)
    # ctx.set_source_rgb(1, 0, 0)
    # stroke_shapes(ctx, 0, 15 * SIZE)


# carregando interface Glade
builder = Gtk.Builder()
builder.add_from_file("view.glade")

# carregando elementos
MainWindow = builder.get_object("MainWindow")
PontoWindow = builder.get_object("PontoWindow")
RetaWindow = builder.get_object("RetaWindow")
PoligonoWindow = builder.get_object("PoligonoWindow")
ExclusaoWindow = builder.get_object("ExclusaoWindow")
AlertaWindow = builder.get_object("AlertaWindow")
DrawingFrame = builder.get_object("DrawingFrame")

objectTreeView = builder.get_object("objectTreeView")


btnPonto = builder.get_object("btnPonto")
btnReta = builder.get_object("btnReta")
btnPoligono = builder.get_object("btnPoligono")
btnUp = builder.get_object("btnUp")
btnDown = builder.get_object("btnDown")
btnLeft = builder.get_object("btnLeft")
btnRight = builder.get_object("btnRight")
btnZoomIn = builder.get_object("btnZoomIn")
btnZoomOut = builder.get_object("btnZoomOut")
btnLimpaTela = builder.get_object("btnLimpaTela")
btnRotacionarDireita = builder.get_object("btnRotacionarDireita")
btnRotacionarEsquerda = builder.get_object("btnRotacionarEsquerda")
btnDeletaItem = builder.get_object("btnDeletaItem")

btnSalvarPonto = builder.get_object("btnSalvarPonto")
btnCancelaPonto = builder.get_object("btnCancelaPonto")
btnSpinX = builder.get_object("btnSpinX")
btnSpinY = builder.get_object("btnSpinY")
textFieldNome = builder.get_object("textFieldNome")

btnSalvarReta = builder.get_object("btnSalvarReta")
btnCancelarReta = builder.get_object("btnCancelarReta")
spinRetaX1 = builder.get_object("spinRetaX1")
spinRetaY1 = builder.get_object("spinRetaY1")
spinRetaX2 = builder.get_object("spinRetaX2")
spinRetaY2 = builder.get_object("spinRetaY2")
textFieldRetaNome = builder.get_object("textFieldRetaNome")

btnConfirmaExclusao = builder.get_object("btnConfirmaExclusao")
btnCancelaExclusao = builder.get_object("btnCancelaExclusao")

poligonoX = builder.get_object("poligonoX")
poligonoY = builder.get_object("poligonoY")
poligonoZ = builder.get_object("poligonoZ")
btnSalvarPoligono = builder.get_object("btnSalvarPoligono")
btnCancelarPoligono = builder.get_object("btnCancelarPoligono")
textFieldPoligonoName = builder.get_object("textFieldPoligonoName")
btnAdicionaPontoPoligono = builder.get_object("btnAdicionaPontoPoligono")

btnWindowAlerta = builder.get_object("btnWindowAlerta")
mensagemTituloAviso = builder.get_object("mensagemTituloAviso")
mensagemAviso = builder.get_object("mensagemAviso")

btnPonto.connect("clicked", onBtnPontoClicked)
DrawingFrame.connect('draw', draw)

builder.connect_signals(Handler())


# exibe tela inicial SGI
MainWindow.show_all()
Gtk.main()


