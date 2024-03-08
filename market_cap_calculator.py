{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 14,
   "id": "6bcae74b-7931-4aba-a6af-040c2e96f917",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "application/vnd.jupyter.widget-view+json": {
       "model_id": "618c763fcdf2441c8c35c383f4d7db6a",
       "version_major": 2,
       "version_minor": 0
      },
      "text/plain": [
       "Text(value='', description='Stock Name:')"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "data": {
      "application/vnd.jupyter.widget-view+json": {
       "model_id": "37c4216335dc4c178293951d7365e7e3",
       "version_major": 2,
       "version_minor": 0
      },
      "text/plain": [
       "FloatText(value=0.0, description='Price/Share:')"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "data": {
      "application/vnd.jupyter.widget-view+json": {
       "model_id": "6735fe76b1ed407d8160766e6e56e1b4",
       "version_major": 2,
       "version_minor": 0
      },
      "text/plain": [
       "FloatText(value=0.0, description='Shares Out:')"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "data": {
      "application/vnd.jupyter.widget-view+json": {
       "model_id": "349167b90e284abc8f06ab811fabe74b",
       "version_major": 2,
       "version_minor": 0
      },
      "text/plain": [
       "FloatText(value=0.0, description='Locked Shares:')"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "data": {
      "application/vnd.jupyter.widget-view+json": {
       "model_id": "c2e82dcb3f25410bb0fc6de39fc9751d",
       "version_major": 2,
       "version_minor": 0
      },
      "text/plain": [
       "Button(description='Calculate', style=ButtonStyle())"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "data": {
      "application/vnd.jupyter.widget-view+json": {
       "model_id": "cee0304000f64d71b0610f4a70f4a4e6",
       "version_major": 2,
       "version_minor": 0
      },
      "text/plain": [
       "Output()"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "import ipywidgets as widgets\n",
    "from IPython.display import display, clear_output\n",
    "from datetime import datetime\n",
    "import csv\n",
    "\n",
    "# Function definitions from previous steps remain the same\n",
    "def calculate_market_cap(price_per_share, shares_outstanding):\n",
    "    return price_per_share * shares_outstanding\n",
    "\n",
    "def calculate_free_float_market_cap(price_per_share, shares_outstanding, locked_shares):\n",
    "    return price_per_share * (shares_outstanding - locked_shares)\n",
    "\n",
    "def categorize_stock(market_cap):\n",
    "    if market_cap > 200e9:\n",
    "        return \"Mega Cap\"\n",
    "    elif market_cap > 10e9:\n",
    "        return \"Large Cap\"\n",
    "    elif market_cap > 2e9:\n",
    "        return \"Mid Cap\"\n",
    "    elif market_cap > 300e6:\n",
    "        return \"Small Cap\"\n",
    "    elif market_cap > 50e6:\n",
    "        return \"Micro Cap\"\n",
    "    else:\n",
    "        return \"Not Categorized\"\n",
    "\n",
    "def log_stock_info(stock_name, market_cap, cap_category):\n",
    "    with open(\"stock_info_log.csv\", \"a\", newline='') as file:\n",
    "        writer = csv.writer(file)\n",
    "        writer.writerow([stock_name, datetime.now().strftime(\"%Y-%m-%d %H:%M:%S\"), market_cap, cap_category])\n",
    "\n",
    "# UI Components\n",
    "stock_name = widgets.Text(description=\"Stock Name:\")\n",
    "price_per_share = widgets.FloatText(description=\"Price/Share:\")\n",
    "shares_outstanding = widgets.FloatText(description=\"Shares Out:\")\n",
    "locked_shares = widgets.FloatText(description=\"Locked Shares:\")\n",
    "calculate_button = widgets.Button(description=\"Calculate\")\n",
    "output = widgets.Output()\n",
    "\n",
    "# Event Handlers\n",
    "def on_calculate_button_clicked(b):\n",
    "    with output:\n",
    "        clear_output()\n",
    "        try:\n",
    "            cap = calculate_market_cap(price_per_share.value, shares_outstanding.value)\n",
    "            free_float_cap = calculate_free_float_market_cap(price_per_share.value, shares_outstanding.value, locked_shares.value)\n",
    "            category = categorize_stock(cap)\n",
    "            log_stock_info(stock_name.value, cap, category)\n",
    "            print(f\"Market Cap: {cap}\\nFree-Float Market Cap: {free_float_cap}\\nCategory: {category}\")\n",
    "        except Exception as e:\n",
    "            print(f\"Error: {e}\")\n",
    "\n",
    "calculate_button.on_click(on_calculate_button_clicked)\n",
    "\n",
    "# Display UI\n",
    "display(stock_name, price_per_share, shares_outstanding, locked_shares, calculate_button, output)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "97a2489e-193d-499a-8e11-910ac1c4bfd4",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.12.1"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
