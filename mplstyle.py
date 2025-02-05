from pathlib import Path
import matplotlib.pyplot as plt


class feng1m8:
    @staticmethod
    def style(style='half'):
        feng1m8.rcParams = plt.rcParams

        plt.rcParams['font.family'] = 'serif'
        plt.rcParams['mathtext.fontset'] = 'dejavuserif'
        plt.rcParams['xtick.top'] = True
        plt.rcParams['xtick.bottom'] = True
        plt.rcParams['xtick.direction'] = 'in'
        plt.rcParams['xtick.minor.visible'] = True
        plt.rcParams['ytick.left'] = True
        plt.rcParams['ytick.right'] = True
        plt.rcParams['ytick.direction'] = 'in'
        plt.rcParams['ytick.minor.visible'] = True
        plt.rcParams['legend.edgecolor'] = 'None'
        plt.rcParams['figure.constrained_layout.use'] = True
        plt.rcParams['savefig.dpi'] = 300
        plt.rcParams['savefig.bbox'] = 'tight'
        plt.rcParams['pdf.compression'] = 9
        plt.rcParams['pdf.fonttype'] = 42

        if style == 'half':
            plt.rcParams['figure.figsize'] = (4.3, 3.2)
        elif style == 'full':
            plt.rcParams['figure.figsize'] = (9.1, 6.8)

        feng1m8.set_layout_engine.function = plt.Figure.set_layout_engine
        plt.Figure.set_layout_engine = feng1m8.set_layout_engine

        feng1m8.colorbar.function = plt.colorbar
        plt.colorbar = feng1m8.colorbar

        feng1m8.savefig.function = plt.savefig
        plt.savefig = feng1m8.savefig

        plt.caption = feng1m8.caption

    @staticmethod
    def set_layout_engine(self, layout=None, **kwargs):
        if layout is None:
            feng1m8.set_layout_engine.function(self, 'compressed', **kwargs)
        else:
            feng1m8.set_layout_engine.function(self, layout, **kwargs)

    @staticmethod
    def colorbar(*args, **kwargs):
        cbar = feng1m8.colorbar.function(*args, **kwargs)
        cbar.ax.tick_params(bottom=True, left=True, which='both')
        return cbar

    @staticmethod
    def savefig(fname, *args, **kwargs):
        if Path(fname).suffix == '.png':
            feng1m8.savefig.function(fname, *args, pad_inches='layout', pil_kwargs={
                'optimize': True,
            }, **kwargs)
        else:
            feng1m8.savefig.function(fname, *args, pad_inches='layout', **kwargs)

    @staticmethod
    def caption(label, loc, bbox_to_anchor=None, **kwargs):
        trans = plt.gca().transAxes

        if bbox_to_anchor is None:
            bbox_to_anchor = {
                'upper right': (1, 1),
                'upper left': (0, 1),
                'lower left': (0, 0),
                'lower right': (1, 0),
                'center left': (0, 0.5),
                'center right': (1, 0.5),
                'upper center': (0.5, 1),
                'lower center': (0.5, 0),
            }[loc]

            trans = plt.gca().transAxes + plt.matplotlib.transforms.ScaledTranslation(
                (1 - 2 * bbox_to_anchor[0]) / 12,
                (1 - 2 * bbox_to_anchor[1]) / 12,
                plt.gcf().dpi_scale_trans,
            )

        loc = loc.split(' ')
        if loc[0] == 'upper':
            loc[0] = 'top'
        elif loc[0] == 'lower':
            loc[0] = 'bottom'

        return plt.text(bbox_to_anchor[0], bbox_to_anchor[1], label, va=loc[0], ha=loc[1], transform=trans, **kwargs)

    @staticmethod
    def use(*style):
        if style[0] == 'feng1m8':
            feng1m8.style(style[1])
        else:
            plt.rcParams = feng1m8.rcParams
            plt.Figure.set_layout_engine = feng1m8.set_layout_engine.function
            plt.colorbar = feng1m8.colorbar.function
            plt.savefig = feng1m8.savefig.function
            feng1m8.use.function(style)


feng1m8.use.function = plt.style.use
plt.style.use = feng1m8.use
