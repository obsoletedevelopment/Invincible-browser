using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace browser_custom
{
    public partial class Form1 : Form
    {

        bool haspaniced = false;
        public Form1()
        {
            InitializeComponent();
            webBrowser1.GoHome();
        }

        private void button1_Click(object sender, EventArgs e)
        {
            
        }

        private void button2_Click(object sender, EventArgs e)
        {
            webBrowser1.GoHome();
        }

        private void Form1_Load(object sender, EventArgs e)
        {

        }

        private void button1_Click_1(object sender, EventArgs e)
        {
            webBrowser1.GoHome();
        }

        private void button2_Click_1(object sender, EventArgs e)
        {

        }

        private void button2_Click_2(object sender, EventArgs e)
        {

        }

        private void panel1_Paint(object sender, PaintEventArgs e)
        {

        }

        private void button2_Click_3(object sender, EventArgs e)
        {
            webBrowser1.GoBack();
        }

        private void button3_Click(object sender, EventArgs e)
        {
            webBrowser1.GoForward();
        }

        private void button4_Click(object sender, EventArgs e)
        {
            if(haspaniced == false)
            {
                panel1.BringToFront();
                haspaniced = true;
            }
            else
            {
                panel1.SendToBack();
                haspaniced = false;
            }
        }

        private void button4_Click_1(object sender, EventArgs e)
        {
            webBrowser1.Refresh();
        }
    }
}
