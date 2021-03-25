using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;
using Microsoft.Web.WebView2.Core;

namespace invincible_2
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void webView21_Click(object sender, EventArgs e)
        {

        }

        private void button2_Click(object sender, EventArgs e)
        {
            webviewpanel.CoreWebView2.Navigate("https://www.google.com");
        }

        private void button1_Click(object sender, EventArgs e)
        {
            webviewpanel.CoreWebView2.Navigate("https://" + textBox1.Text);
        }

        private void button4_Click(object sender, EventArgs e)
        {
            webviewpanel.CoreWebView2.GoForward();
        }

        private void button5_Click(object sender, EventArgs e)
        {
            webviewpanel.CoreWebView2.GoBack();
        }

        private void button3_Click(object sender, EventArgs e)
        {
            webviewpanel.CoreWebView2.Reload();
        }
    }
}
