 #ifndef RENDERWINDOW_H
#define RENDERWINDOW_H

#include <QWidget>

namespace Ui {
class RenderWindow;
}

class RenderWindow : public QWidget
{
    Q_OBJECT

public:
    explicit RenderWindow(QWidget *parent = 0);
    ~RenderWindow();

private:
    Ui::RenderWindow *ui;
};

#endif // RENDERWINDOW_H
