#ifndef MAINWINDOW_H
#define MAINWINDOW_H

#include <QMainWindow>
#include <QDebug>

namespace Ui {
class MainWindow;
}

class MainWindow : public QMainWindow
{
    Q_OBJECT

public:
    explicit MainWindow(QWidget *parent = 0);
    ~MainWindow();

public slots:
    void test();

    void updateLength(int val);
    void updateWidth(int val);
    void updateHeight(int val);
    void updatePercentFillingBox(double val);
    void updateNumberObjectsWanted(int val);
    void updateServerAdress(QString val);

    void process();
    void testServer();

private:
    Ui::MainWindow *ui;

    int length = 50;
    int width = 50;
    int height = 50;
    double percentFillingBox = 0.6;
    int numberObjectsWanted = 20;
    QString serverAdress = "localhost:8000";
};

#endif // MAINWINDOW_H
