﻿using System;
using System.ComponentModel.DataAnnotations;

namespace RazorSpacesMovie.Models
{

    public class Movie
    {
        public int ID { get; set; }
        public string Title { get; set; }

        [DataType(DataType.Date)]
        public DateTime ReleaseDate { get; set; }
        public String Genre { get; set; }
        public Decimal Price { get; set; }
    }
}