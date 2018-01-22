/* -*- c++ -*- */
/* 
 * Copyright 2018 <+YOU OR YOUR COMPANY+>.
 * 
 * This is free software; you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation; either version 3, or (at your option)
 * any later version.
 * 
 * This software is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 * 
 * You should have received a copy of the GNU General Public License
 * along with this software; see the file COPYING.  If not, write to
 * the Free Software Foundation, Inc., 51 Franklin Street,
 * Boston, MA 02110-1301, USA.
 */

#ifdef HAVE_CONFIG_H
#include "config.h"
#endif

#include <gnuradio/io_signature.h>
#include "preamble_detector_impl.h"

namespace gr {
  namespace misc {

    preamble_detector::sptr
    preamble_detector::make(unsigned char *data, int preamble_length, int message_lenght)
    {
      return gnuradio::get_initial_sptr
        (new preamble_detector_impl(data, preamble_length, message_lenght));
    }

    /*
     * The private constructor
     */
    preamble_detector_impl::preamble_detector_impl(unsigned char *data, int preamble_length, int message_lenght)
      : gr::block("preamble_detector",
              gr::io_signature::make(1, 1, sizeof(char)),
              gr::io_signature::make(1, 1, sizeof(char)))
    {
			sequence  = new char[preamble_length]; 		
			sequence_length = preamble_length;					
			for(int i  = 0; i < preamble_length; i++)
				sequence[i] = data[i];
			sequence_detected = false;
			counter = 0;																
			message_counter = 0;												
			m_length = message_lenght;									
		}

    /*
     * Our virtual destructor.
     */
    preamble_detector_impl::~preamble_detector_impl()
    {
			delete[] sequence;
    }

    void
    preamble_detector_impl::forecast (int noutput_items, gr_vector_int &ninput_items_required)
    {
      /* <+forecast+> e.g. ninput_items_required[0] = noutput_items */
			unsigned ninputs = ninput_items_required.size();
			for(unsigned i = 0; i < ninputs ; i++)
      	ninput_items_required[i] = noutput_items;
    }

    int
    preamble_detector_impl::general_work (int noutput_items,
                       gr_vector_int &ninput_items,
                       gr_vector_const_void_star &input_items,
                       gr_vector_void_star &output_items)
    {
      const char *in = (const char *) input_items[0];
      char *out = (char *) output_items[0];
			int n = ninput_items[0];
			int i = 0;
			//int history = 0;	
      // Do <+signal processing+>
      // Tell runtime system how many input items we consumed on
      // each input stream.
		while(n > 0)
		{
			if(!sequence_detected) // Séquence non détectée
			{
				if(in[i] == sequence[counter]) // Identification du préambule
				{
					counter++;
				}
				else 
				{
					counter = 0;
				}
				if(counter == sequence_length) // Préambule identifié
				{
					sequence_detected = true;
					counter = 0;
				}
				else // Préambule non identifié
				{
					out[i] = 0; //A changer                    
				}
				n--;
			}
			else // Séquence détecté
			{
				out[i] = in[i];
				if(message_counter < (m_length - 1)) // Identification du message
				{
					message_counter++;
					 //A changer                        
				}
				else
				{
					message_counter = 0;
					sequence_detected = false;
				}
				n--;
			}
			i++;
		}
      consume_each (noutput_items);

      // Tell runtime system how many output items we produced.
      return noutput_items;
    }

  } /* namespace misc */
} /* namespace gr */

