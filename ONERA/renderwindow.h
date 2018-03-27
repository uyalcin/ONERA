 #ifndef RENDERWINDOW_H
#define RENDERWINDOW_H

#include <QWidget>
#include "box.h"
#include <vector>
#include <QDebug>

namespace Ui {
class RenderWindow;
}

class RenderWindow : public QWidget
{
    Q_OBJECT

public:
    explicit RenderWindow(QWidget *parent = 0);
    ~RenderWindow();

    void setDataSet(std::vector<Box> boxs);

private:
    Ui::RenderWindow *ui;
};

#endif // RENDERWINDOW_H
